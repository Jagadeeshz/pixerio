/* Pixerio — v3.0 "Motion" interaction layer
   Motion vocabulary sourced from uxfolio.io and rebuilt here with no
   dependencies, behind the same guarantees px.js gives:
     · with JS off every page still renders, reads and navigates
     · html[data-motion="paused"] (the header toggle) freezes everything
     · prefers-reduced-motion removes the movement, not the content
   Each block is independent: if one selector is missing on a page it is a
   no-op, never an error. */
(function () {
  'use strict';

  var root = document.documentElement,
      reduce = matchMedia('(prefers-reduced-motion: reduce)'),
      fine = matchMedia('(hover:hover) and (pointer:fine)'),
      KEY = 'pixerio:motion';

  function paused() {
    return root.getAttribute('data-motion') === 'paused' || reduce.matches;
  }

  /* ======================================================================
     1. page transition — fade out on internal navigation, fade in on arrival
     Only same-folder .html links. External, mail, tel, hash and download
     links navigate normally.
     ====================================================================== */
  root.classList.remove('pt-out'); /* bfcache / back button */
  addEventListener('pageshow', function () { root.classList.remove('pt-out'); });

  document.addEventListener('click', function (e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target.closest && e.target.closest('a');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    if (!href || a.target === '_blank' || a.hasAttribute('download')) return;
    if (/^(#|mailto:|tel:|https?:|\/\/)/i.test(href)) return;
    if (!/\.html(\?|#|$)/i.test(href)) return;
    if (paused()) return;
    e.preventDefault();
    root.classList.add('pt-out');
    /* leave on the frame the fade finishes, so the swap is never visible */
    setTimeout(function () { location.href = href; }, 190);
  });

  /* ======================================================================
     2. marker highlight — the uxfolio swash, on the emphasis word of a heading
     The word is already <em> in the markup (the design's existing "this part
     matters" signal). No markup is rewritten, so search engines, screen
     readers and print see exactly the same text.
     ====================================================================== */
  var marks = [].slice.call(document.querySelectorAll('.page-head h1 em, h1 em, h2 em'));
  marks.forEach(function (em) {
    if (em.querySelector('img,svg')) return;
    em.classList.add('m-mark');
  });
  if (marks.length) {
    if (!('IntersectionObserver' in window) || reduce.matches) {
      marks.forEach(function (m) { m.classList.add('in'); });
    } else {
      var ioMark = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          /* delay after the line itself has risen, like the source site: the
             heading lands first, then the marker draws under it */
          setTimeout(function () { en.target.classList.add('in'); }, 320);
          ioMark.unobserve(en.target);
        });
      }, { threshold: 0.6 });
      marks.forEach(function (m) { ioMark.observe(m); });
    }
  }

  /* ======================================================================
     3. hero deck — three cards, one shuffle
     uxfolio animates this in pure CSS with a 3-step keyframe loop. A timer
     does the same thing here with transitions, which makes it pausable:
     on hover, on the page's motion toggle, when the deck scrolls away, and
     when the tab is hidden.
     ====================================================================== */
  var deck = document.querySelector('[data-deck]');
  if (deck) {
    var cards = [].slice.call(deck.querySelectorAll('.deck__card')),
        slots = ['center', 'left', 'right'],
        step = 0,
        timer = null,
        visible = true;

    function paint() {
      cards.forEach(function (c, i) {
        c.setAttribute('data-pos', slots[(i + step) % 3]);
      });
    }
    function run() {
      stop();
      if (paused() || !visible || document.hidden || cards.length < 3 || !fine.matches) return;
      timer = setInterval(function () { step++; paint(); }, 3600);
    }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }

    paint();
    run();
    deck.addEventListener('mouseenter', stop);
    deck.addEventListener('mouseleave', run);
    document.addEventListener('visibilitychange', run);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) {
        visible = en[0].isIntersecting;
        run();
      }, { threshold: 0.15 }).observe(deck);
    }
    /* the header motion toggle and the OS setting both change mid-session */
    if (reduce.addEventListener) reduce.addEventListener('change', run);
    new MutationObserver(run).observe(root, { attributes: true, attributeFilter: ['data-motion'] });
    addEventListener('resize', run, { passive: true });
  }

  /* ======================================================================
     4. stacking panels — a pinned card dims and scales as the next one covers
     ====================================================================== */
  var stack = [].slice.call(document.querySelectorAll('.process__col .step'));
  if (stack.length) {
    var pending = false;
    function paintStack() {
      pending = false;
      stack.forEach(function (el) {
        var top = parseFloat(getComputedStyle(el).top) || 0;
        var r = el.getBoundingClientRect();
        el.classList.toggle('is-stuck', !reduce.matches && r.top <= top + 2);
      });
    }
    function onScroll() {
      if (pending) return;
      pending = true;
      requestAnimationFrame(paintStack);
    }
    addEventListener('scroll', onScroll, { passive: true });
    addEventListener('resize', onScroll, { passive: true });
    paintStack();
  }

  /* ======================================================================
     5. FAQ — grow the answer instead of snapping it open
     <details> stays the real control: keyboard, find-in-page and no-JS all
     keep working. We only move the inner content into a box we can measure.
     ====================================================================== */
  if (!reduce.matches) {
    [].slice.call(document.querySelectorAll('.faq details')).forEach(function (d) {
      if (d.dataset.grow === 'yes') return;
      var body = document.createElement('div');
      body.className = 'faq__body';
      while (d.lastElementChild && d.lastElementChild.tagName !== 'SUMMARY') {
        body.insertBefore(d.lastElementChild, body.firstChild);
      }
      if (!body.firstChild) return;
      d.appendChild(body);
      d.dataset.grow = 'yes';

      var sum = d.querySelector('summary');
      if (!sum) return;
      sum.addEventListener('click', function (e) {
        e.preventDefault();
        if (d.dataset.anim === 'yes') return;
        d.dataset.anim = 'yes';
        var target = body.scrollHeight;
        if (d.open) {
          body.style.height = target + 'px';
          body.offsetHeight; /* flush */
          body.style.height = '0px';
          setTimeout(function () {
            d.open = false;
            d.dataset.anim = 'no';
            body.style.height = '';
          }, 420);
        } else {
          d.open = true;
          body.style.height = '0px';
          body.offsetHeight;
          body.style.height = target + 'px';
          setTimeout(function () {
            d.dataset.anim = 'no';
            body.style.height = 'auto';
          }, 420);
        }
      });
    });
  }

  /* ======================================================================
     6. stagger — give siblings in a grid an index so they cascade
     px.js already reveals these blocks; this only sets --i, which the CSS
     delay uses. Applies to data-reveal children of a grid or list.
     ====================================================================== */
  [].slice.call(document.querySelectorAll('.work, .cards, .quotes, .bento, .faq, .stats, .rows'))
    .forEach(function (box) {
      [].slice.call(box.querySelectorAll('[data-reveal]')).forEach(function (el, i) {
        if (!el.style.getPropertyValue('--i')) el.style.setProperty('--i', String(i % 6));
      });
    });

  /* ======================================================================
     7. marquee rails — duplicate the track so the loop is seamless
     ====================================================================== */
  [].slice.call(document.querySelectorAll('.mq__track')).forEach(function (track) {
    if (track.dataset.cloned === 'yes') return;
    track.innerHTML += track.innerHTML;
    track.dataset.cloned = 'yes';
  });
})();
