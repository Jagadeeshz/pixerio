/* Pixerio — hero stage (v10.1)
   ---------------------------------------------------------------------------
   A three-act composition on one clock, rebuilt from the reference clip:

     1  fragmented   0.0 - 6.0s   six panels travel through the frame, each at its
                                  own angle and height; nothing lines up
     2  transform    6.0 - 13.5s  a spectrum trail sweeps left to right; every
                                  panel it passes squares up and resolves from
                                  its problem state to its solution state
     3  connected   13.5 - 19.0s  the panels close into one lattice, connectors
                                  draw between them, the trail flows through
     4  loop        19.0 - 21.0s  the composition exhales and the cycle restarts

   No library. Panels are DOM nodes (crisp text, real links elsewhere on the
   page); the canvas only paints the spectrum ribbons, connectors and trail.

   Stops dead on: prefers-reduced-motion, the header "Pause motion" control,
   a hidden tab, or the hero scrolling out of view. In every stopped state the
   resolved composition is what you see, never a half-faded frame.
   --------------------------------------------------------------------------- */
(function () {
  'use strict';

  var stage = document.querySelector('.stage[data-stage]');
  if (!stage) return;

  var panels = [].slice.call(stage.querySelectorAll('.stg-panel'));
  var canvas = stage.querySelector('.stage__canvas');
  var light = stage.querySelector('.stage__light');
  var bar = document.querySelector('.stage__bar i');
  var caption = document.querySelector('[data-stage-caption]');
  if (!panels.length) return;

  var root = document.documentElement,
      reduce = window.matchMedia('(prefers-reduced-motion: reduce)'),
      ctx = canvas.getContext('2d'),
      lctx = light ? light.getContext('2d') : null,
      W = 0, H = 0, dpr = Math.min(window.devicePixelRatio || 1, 2),
      raf = null, start = null, t = 0, visible = true, reduced = reduce.matches;

  var T = 21.0;                       /* loop length                       */
  var A1 = 6.0, A2 = 13.5, A3 = 19.0; /* act boundaries                    */

  /* act 2 target: a symmetric fan, tight pair in the centre */
  var FOCUS = [
    { x: -0.560, y: -0.16, ry:  66, s: 0.68 },
    { x: -0.320, y: -0.06, ry:  42, s: 0.80 },
    { x: -0.095, y:  0.03, ry:   8, s: 0.96 },
    { x:  0.095, y:  0.03, ry:  -8, s: 0.96 },
    { x:  0.320, y: -0.06, ry: -42, s: 0.80 },
    { x:  0.560, y: -0.16, ry: -66, s: 0.68 }
  ];
  /* act 3 target: one connected lattice, three over three */
  var GRID = [
    { x: -0.250, y: -0.250, ry:  14, s: 0.80 },
    { x:  0.000, y: -0.262, ry:   0, s: 0.84 },
    { x:  0.250, y: -0.250, ry: -14, s: 0.80 },
    { x: -0.250, y:  0.250, ry:  14, s: 0.80 },
    { x:  0.000, y:  0.262, ry:   0, s: 0.84 },
    { x:  0.250, y:  0.250, ry: -14, s: 0.80 }
  ];

  var CAPTIONS = [
    ['01', 'Six separate problems'],
    ['02', 'One spectrum, passing through'],
    ['03', 'One connected partner']
  ];

  function clamp(v, a, b) { return v < a ? a : v > b ? b : v; }
  function lerp(a, b, u) { return a + (b - a) * u; }
  function ease(u) { return u < 0.5 ? 2 * u * u : 1 - Math.pow(-2 * u + 2, 2) / 2; }

  function paused() {
    return root.getAttribute('data-motion') === 'paused';
  }

  function resize() {
    var r = stage.getBoundingClientRect();
    W = r.width; H = r.height;
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.max(1, Math.round(W * dpr));
    canvas.height = Math.max(1, Math.round(H * dpr));
    canvas.style.width = W + 'px';
    canvas.style.height = H + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    if (lctx) {
      light.width = canvas.width;
      light.height = canvas.height;
      light.style.width = W + 'px';
      light.style.height = H + 'px';
      lctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
  }

  /* The stage is the whole band; the composition lives inside a spread that
     stays clear of the copy column and clips nowhere — the mask does the
     fading, so panels never need a box to hide behind. */
  function spread() {
    return { x: Math.min(W * 0.52, 760), y: Math.min(H * 0.78, 520) };
  }

  function setPanel(el, o) {
    var sp = spread();
    el.style.setProperty('--x', (o.x * sp.x).toFixed(1) + 'px');
    el.style.setProperty('--y', (o.y * sp.y).toFixed(1) + 'px');
    el.style.setProperty('--z', ((o.s - 0.8) * 120).toFixed(1) + 'px');
    el.style.setProperty('--ry', o.ry.toFixed(2) + 'deg');
    el.style.setProperty('--s', o.s.toFixed(3));
    el.style.setProperty('--op', o.op.toFixed(3));
    el.style.setProperty('--sat', o.solved ? '1' : '0.62');
    el.style.setProperty('--con', o.solved ? '1.04' : '0.94');
    el.style.setProperty('--blur', (o.blur || 0).toFixed(2));
    if (o.solved) el.setAttribute('data-solved', '1');
    else el.removeAttribute('data-solved');
    el.style.zIndex = String(10 + Math.round(o.s * 10));
  }

  /* ---------------- the three acts ---------------- */
  function stateAt(i, time) {
    var p = panels[i], u, a, b, o;

    /* act 1 — a conveyor: six panels spread across the stage, each on its own
       angle and height, sliding right to left and fading at the edges */
    if (time < A1) return act1Pos(i, time);

    /* act 2 — converge to the fan; each panel resolves as the trail passes it */
    var trailX = lerp(-0.62, 0.62, clamp((time - A1) / 5.6, 0, 1));
    var passAt = FOCUS[i].x;
    var solved = time >= A1 + 0.35 && trailX >= passAt - 0.02;

    if (time < A2) {
      u = ease(clamp((time - A1 - i * 0.22) / 3.4, 0, 1));
      var f1 = { x: lerp(1.30, -0.62, 1), y: (i % 2 ? 0.03 : -0.02), ry: -70 * Math.cos(0), s: 0.66 };
      /* start from wherever act 1 left it */
      var start = act1End(i);
      return {
        x: lerp(start.x, FOCUS[i].x, u),
        y: lerp(start.y, FOCUS[i].y, u),
        ry: lerp(start.ry, FOCUS[i].ry, u),
        s: lerp(start.s, FOCUS[i].s, u),
        op: 1,
        solved: solved,
        blur: (1 - u) * 0.4
      };
    }

    /* act 3 — close into the lattice */
    u = ease(clamp((time - A2) / 3.0, 0, 1));
    var from = FOCUS[i], to = GRID[i];
    return {
      x: lerp(from.x, to.x, u),
      y: lerp(from.y, to.y, u) + Math.sin(time * 0.9 + i) * 0.004 * (1 - u),
      ry: lerp(from.ry, to.ry, u),
      s: lerp(from.s, to.s, u),
      op: 1,
      solved: true,
      blur: 0
    };
  }

  function act1Pos(i, time) {
    var u = ((time / A1) + i / panels.length) % 1;
    var edge = Math.min(u, 1 - u);
    return {
      x: lerp(0.80, -0.80, u),
      y: Math.sin(u * Math.PI * 2 + i * 1.7) * 0.05 + (i % 2 ? 0.045 : -0.03),
      ry: 60 * Math.cos(u * Math.PI * 2.2) + Math.sin(u * 9 + i) * 8,
      s: 0.74 + 0.16 * Math.sin(u * Math.PI),
      op: clamp(edge / 0.10, 0, 1),
      solved: false,
      blur: Math.abs(Math.cos(u * Math.PI * 2.2)) > 0.72 ? 0.8 : 0
    };
  }

  /* where act 1 left panel i, so act 2 continues from it */
  function act1End(i) { return act1Pos(i, A1); }

  /* ---------------- canvas: ribbons, connectors, trail ---------------- */
  function colours(el) {
    var c = getComputedStyle(el);
    return [c.getPropertyValue('--g1'), c.getPropertyValue('--g2'), c.getPropertyValue('--g3')];
  }

  function ribbon(x, y, h, ry, cols, alpha) {
    var skew = clamp(Math.abs(ry) / 90, 0, 1);
    var w = 26 + 44 * skew;
    var bend = (ry > 0 ? -1 : 1) * (18 + 34 * skew);
    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    ctx.globalAlpha = alpha;
    var g = ctx.createLinearGradient(x - w, y - h / 2, x + w, y + h / 2);
    g.addColorStop(0, cols[0] || 'rgba(0,179,189,.9)');
    g.addColorStop(0.45, cols[1] || 'rgba(33,127,195,.9)');
    g.addColorStop(1, cols[2] || 'rgba(73,173,72,.9)');
    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.moveTo(x - w, y - h / 2);
    ctx.bezierCurveTo(x - w + bend, y - h / 4, x - w - bend, y + h / 4, x - w, y + h / 2);
    ctx.lineTo(x + w, y + h / 2);
    ctx.bezierCurveTo(x + w + bend, y + h / 4, x + w - bend, y - h / 4, x + w, y - h / 2);
    ctx.closePath();
    ctx.filter = 'blur(6px)';
    ctx.fill();
    ctx.restore();
  }

  function trail(x, y0, y1, alpha) {
    if (!lctx) return;
    var c2 = lctx, prev = ctx;
    var g = lctx.createLinearGradient(x - 90, 0, x + 90, 0);
    g.addColorStop(0, 'rgba(0,179,189,0)');
    g.addColorStop(0.2, 'rgba(0,179,189,.55)');
    g.addColorStop(0.45, 'rgba(33,127,195,.85)');
    g.addColorStop(0.6, 'rgba(73,173,72,.8)');
    g.addColorStop(0.8, 'rgba(184,213,80,.55)');
    g.addColorStop(1, 'rgba(184,213,80,0)');
    prev.save();
    prev.globalCompositeOperation = 'lighter';
    prev.globalAlpha = alpha;
    prev.fillStyle = 'rgba(0,0,0,0)';
    prev.restore();
    c2.save();
    c2.globalCompositeOperation = 'lighter';
    c2.globalAlpha = alpha;
    c2.fillStyle = g;
    c2.filter = 'blur(12px)';
    c2.fillRect(x - 90, y0, 180, y1 - y0);
    c2.globalAlpha = alpha * 0.55;
    c2.fillStyle = 'rgba(255,255,255,.9)';
    c2.filter = 'blur(5px)';
    c2.fillRect(x - 30, y0, 60, y1 - y0);
    c2.filter = 'none';
    c2.restore();
  }

  function flow(x0, x1, y, alpha) {
    if (!lctx) return;
    var g = lctx.createLinearGradient(x0, y, x1, y);
    g.addColorStop(0, 'rgba(0,179,189,0)');
    g.addColorStop(0.18, 'rgba(0,179,189,.55)');
    g.addColorStop(0.42, 'rgba(33,127,195,.8)');
    g.addColorStop(0.58, 'rgba(73,173,72,.8)');
    g.addColorStop(0.8, 'rgba(184,213,80,.5)');
    g.addColorStop(1, 'rgba(184,213,80,0)');
    lctx.save();
    lctx.globalCompositeOperation = 'lighter';
    lctx.globalAlpha = alpha;
    lctx.fillStyle = g;
    lctx.filter = 'blur(7px)';
    lctx.fillRect(x0, y - 5, x1 - x0, 10);
    lctx.restore();
  }

  function connector(ax, ay, bx, by, alpha) {
    var ctx2 = lctx || ctx;
    ctx2.save();
    ctx2.globalCompositeOperation = 'lighter';
    ctx2.globalAlpha = alpha;
    ctx2.strokeStyle = 'rgba(255,255,255,.55)';
    ctx2.lineWidth = 1.1;
    ctx2.setLineDash([3, 7]);
    ctx2.beginPath();
    ctx2.moveTo(ax, ay);
    ctx2.bezierCurveTo((ax + bx) / 2, ay, (ax + bx) / 2, by, bx, by);
    ctx2.stroke();
    ctx2.restore();
  }

  function connectorOld(ax, ay, bx, by, alpha) {
    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    ctx.globalAlpha = alpha;
    ctx.strokeStyle = 'rgba(33,127,195,.55)';
    ctx.lineWidth = 1.3;
    ctx.setLineDash([4, 6]);
    ctx.beginPath();
    ctx.moveTo(ax, ay);
    ctx.bezierCurveTo((ax + bx) / 2, ay, (ax + bx) / 2, by, bx, by);
    ctx.stroke();
    ctx.restore();
  }

  function draw(time) {
    ctx.clearRect(0, 0, W, H);
    if (lctx) lctx.clearRect(0, 0, W, H);
    var cx = W / 2, cy = H / 2;
    var mid = clamp((time - A2) / 2.2, 0, 1);

    /* ribbons behind the panels that are turned away from camera */
    panels.forEach(function (el, i) {
      var st = stateAt(i, time);
      if (st.op < 0.05) return;
      var sk = Math.abs(st.ry) / 90;
      if (sk < 0.55) return;
      ribbon(cx + st.x * W, cy + st.y * H, H * 0.52 * st.s,
             st.ry, colours(el), (sk - 0.55) * 0.9 * st.op);
    });

    /* connectors once the lattice closes */
    if (mid > 0.02) {
      var pts = panels.map(function (el, i) {
        var st = stateAt(i, time);
        return [cx + st.x * W, cy + st.y * H];
      });
      for (var k = 0; k < 3; k++) {
        connector(pts[k][0], pts[k][1], pts[k + 3][0], pts[k + 3][1], mid * 0.5);
      }
      connector(pts[0][0], pts[0][1], pts[1][0], pts[1][1], mid * 0.3);
      connector(pts[1][0], pts[1][1], pts[2][0], pts[2][1], mid * 0.3);
    }

    /* the spectrum trail */
    if (time >= A1) {
      if (time < A2) {
        var tx = cx + lerp(-0.62, 0.62, clamp((time - A1) / 5.6, 0, 1)) * W;
        trail(tx, cy - H * 0.34, cy + H * 0.34, 0.95);
      } else {
        /* act 3: the spectrum runs through the seam of the lattice and breathes */
        var pulse = 0.35 + 0.18 * Math.sin((time - A2) * 1.8);
        flow(cx - W * 0.40, cx + W * 0.40, cy, pulse * mid);
        flow(cx - W * 0.40, cx + W * 0.40, cy - H * 0.205, pulse * mid * 0.5);
      }
    }
  }

  /* ---------------- loop ---------------- */
  function render(time) {
    t = time;
    for (var i = 0; i < panels.length; i++) setPanel(panels[i], stateAt(i, time));
    draw(time);

    if (bar) bar.style.width = ((time / T) * 100).toFixed(1) + '%';
    if (caption) {
      var act = time < A1 ? 0 : time < A2 ? 1 : 2;
      var c = CAPTIONS[act];
      caption.innerHTML = '<b>' + c[0] + '</b> ' + c[1];
    }
  }

  function tick(ts) {
    if (start === null) start = ts;
    var time = ((ts - start) / 1000) % T;
    /* act 4: the composition exhales before the next pass */
    var fade = time > A3 ? 1 - clamp((time - A3) / (T - A3 - 0.25), 0, 1) : 1;
    panels.forEach(function (el) {
      if (time > A3) el.style.opacity = (fade * 1).toFixed(3);
      else el.style.removeProperty('opacity');
    });
    render(time);
    raf = requestAnimationFrame(tick);
  }

  function staticFrame() {
    var time = A2 + 2.2;                /* resolved lattice, trail through the middle */
    panels.forEach(function (el, i) {
      var st = stateAt(i, time);
      st.solved = true; st.op = 1; st.blur = 0;
      setPanel(el, st);
    });
    if (bar) bar.style.width = '100%';
    if (caption) caption.innerHTML = '<b>03</b> One connected partner';
    draw(time);
  }

  function stop() {
    if (raf) { cancelAnimationFrame(raf); raf = null; }
  }

  function play() {
    stop();
    if (reduced || paused() || !visible || document.hidden) { staticFrame(); return; }
    start = null;
    raf = requestAnimationFrame(tick);
  }

  /* ---------------- wiring ---------------- */
  stage.setAttribute('data-ready', '1');
  resize();
  play();

  addEventListener('resize', function () {
    resize();
    if (!raf) staticFrame();
  }, { passive: true });

  document.addEventListener('visibilitychange', play);

  if (reduce.addEventListener) {
    reduce.addEventListener('change', function () { reduced = reduce.matches; play(); });
  }

  new MutationObserver(function () { play(); })
    .observe(root, { attributes: true, attributeFilter: ['data-motion'] });

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
      play();
    }, { threshold: 0.05 }).observe(stage);
  }

  /* exposed so the paused / reduced states can be verified without a clock */
  window.PixerioStage = {
    state: function () { return { t: t, panels: panels.map(function (p) { return p.getAttribute('data-solved'); }) }; },
    frame: function (time) { render(time); },
    pause: function () { stop(); },
    play: play
  };
})();
