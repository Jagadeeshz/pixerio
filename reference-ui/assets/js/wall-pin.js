/* ==========================================================================
   Pixerio — the six-service wall as a pinned scroll sequence
   --------------------------------------------------------------------------
   Turns the home wall into one horizontal track driven by vertical scroll:
   the band pins, the cards travel past the stage, and whichever card is at the
   centre comes up to full colour.

   Everything here is additive and reversible. If the viewport is narrow, the
   visitor asks for reduced motion, or JS never runs, this file does nothing and
   the wall stays the grid that build_site.py already wrote. No content is
   duplicated into a shadow DOM: the cards, their links and their text stay
   exactly where they were.
   ========================================================================== */
(function () {
  "use strict";

  var wall = document.querySelector(".wall");
  if (!wall) return;

  var section = wall.closest(".band");
  var cards = Array.prototype.slice.call(wall.children);
  if (!section || cards.length < 4) return;

  var reduce = matchMedia("(prefers-reduced-motion: reduce)");
  var wide = matchMedia("(min-width:1024px)");

  var on = false;
  var targets = [];
  var max = 0;
  var stage = 0;
  var top = 0;
  var span = 0;
  var bar = null;
  var now = null;
  var nameEl = null;
  var raf = 0;

  function clamp(v, lo, hi) { return v < lo ? lo : v > hi ? hi : v; }
  function pad(n) { return (n < 10 ? "0" : "") + n; }

  function buildProgress() {
    var p = document.createElement("div");
    p.className = "wall-progress";
    p.setAttribute("aria-hidden", "true");
    p.innerHTML =
      '<span class="wall-progress__now">01</span>' +
      '<span class="wall-progress__bar"><i></i></span>' +
      '<span class="wall-progress__name"></span>' +
      '<span>/ ' + pad(cards.length) + '</span>';
    wall.parentElement.appendChild(p);
    bar = p.querySelector("i");
    now = p.querySelector(".wall-progress__now");
    nameEl = p.querySelector(".wall-progress__name");
  }

  /* Measured with the transform removed, because a transformed element reports
     transformed rects and the targets would drift on every resize. */
  function measure() {
    wall.style.transform = "none";
    stage = wall.parentElement.clientWidth;
    var wr = wall.getBoundingClientRect();
    max = Math.max(0, wall.scrollWidth - stage);

    targets = cards.map(function (c) {
      var r = c.getBoundingClientRect();
      var centre = (r.left - wr.left) + r.width / 2 - stage / 2;
      return clamp(centre, 0, max);
    });

    var rect = section.getBoundingClientRect();
    top = rect.top + window.scrollY;
    span = Math.max(1, section.offsetHeight - window.innerHeight);
  }

  function render() {
    raf = 0;
    var p = clamp((window.scrollY - top) / span, 0, 1);
    var idx = p * (cards.length - 1);
    var i0 = Math.floor(idx);
    var i1 = Math.min(cards.length - 1, i0 + 1);
    var f = idx - i0;
    var tx = targets[i0] + (targets[i1] - targets[i0]) * f;

    wall.style.transform = "translate3d(" + (-tx).toFixed(2) + "px,0,0)";

    /* Highlight whatever is actually nearest the centre of the stage, not the
       value the scroll maths says — the clamped ends would otherwise light up a
       card that never reaches the middle. */
    var live = 0;
    var best = Infinity;
    targets.forEach(function (t, i) {
      var d = Math.abs(t - tx);
      if (d < best) { best = d; live = i; }
    });
    cards.forEach(function (c, i) { c.classList.toggle("is-live", i === live); });

    if (bar) {
      bar.style.width = (p * 100).toFixed(2) + "%";
      now.textContent = pad(live + 1);
      var h = cards[live].querySelector("h3, h4");
      nameEl.textContent = h ? h.textContent : "";
    }
  }

  function queue() { if (!raf) raf = requestAnimationFrame(render); }

  function enable() {
    if (on) return;
    on = true;
    section.classList.add("band--pin");
    wall.classList.add("wall--track");
    section.style.height =
      Math.round(window.innerHeight * (1 + (cards.length - 1) * 0.55)) + "px";
    if (!bar) buildProgress();
    measure();
    window.addEventListener("scroll", queue, { passive: true });
    window.addEventListener("resize", onResize);
    queue();
  }

  function disable() {
    if (!on) return;
    on = false;
    section.classList.remove("band--pin");
    wall.classList.remove("wall--track");
    section.style.height = "";
    wall.style.transform = "";
    cards.forEach(function (c) { c.classList.remove("is-live"); });
    document.querySelectorAll(".wall-progress").forEach(function (n) { n.remove(); });
    bar = now = nameEl = null;
    window.removeEventListener("scroll", queue);
    window.removeEventListener("resize", onResize);
  }

  var rt = 0;
  function onResize() {
    clearTimeout(rt);
    rt = setTimeout(function () {
      if (!on) return;
      section.style.height =
        Math.round(window.innerHeight * (1 + (cards.length - 1) * 0.55)) + "px";
      measure();
      render();
    }, 160);
  }

  function sync() { (wide.matches && !reduce.matches) ? enable() : disable(); }

  /* Images size the cards; measure again once they are in. */
  window.addEventListener("load", function () { if (on) { measure(); render(); } });

  if (wide.addEventListener) {
    wide.addEventListener("change", sync);
    reduce.addEventListener("change", sync);
  } else {
    wide.addListener(sync);
    reduce.addListener(sync);
  }

  sync();
})();
