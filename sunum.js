/* Brain Rot mu? — slayt gösterici: ok tuşları, kaydırma, #numara bağlantısı, tam ekran */
(function () {
  "use strict";
  var slaytlar = Array.prototype.slice.call(document.querySelectorAll(".slide"));
  var n = slaytlar.length;
  var sahne = document.getElementById("sahne");
  var kayar = document.getElementById("kayar");
  var sayac = document.getElementById("sayac");
  var onceki = document.getElementById("onceki");
  var sonraki = document.getElementById("sonraki");
  var i = 0;

  function olcekle() {
    var w = sahne.clientWidth - 24, h = sahne.clientHeight - 24;
    var s = Math.max(0.05, Math.min(w / 1920, h / 1080));
    kayar.style.transform = "translate(-50%, -50%) scale(" + s + ")";
  }

  function goster(k) {
    i = Math.max(0, Math.min(n - 1, k));
    for (var j = 0; j < n; j++) {
      slaytlar[j].classList.toggle("aktif", j === i);
      slaytlar[j].setAttribute("aria-hidden", j === i ? "false" : "true");
    }
    sayac.textContent = (i + 1) + " / " + n;
    onceki.disabled = i === 0;
    sonraki.disabled = i === n - 1;
    var hedef = "#" + (i + 1);
    if (location.hash !== hedef) {
      try { history.replaceState(null, "", hedef); } catch (e) { /* dosyadan açılınca */ }
    }
  }

  function hashten() {
    var k = parseInt(location.hash.slice(1), 10);
    goster(isNaN(k) ? 0 : k - 1);
  }

  function tamEkran() {
    var d = document, el = d.documentElement;
    if (!d.fullscreenElement && !d.webkitFullscreenElement) {
      var ac = el.requestFullscreen || el.webkitRequestFullscreen;
      if (ac) ac.call(el);
    } else {
      var kapat = d.exitFullscreen || d.webkitExitFullscreen;
      if (kapat) kapat.call(d);
    }
  }

  function tamDegisti() {
    document.body.classList.toggle("tam", !!(document.fullscreenElement || document.webkitFullscreenElement));
    olcekle();
  }

  onceki.addEventListener("click", function () { goster(i - 1); });
  sonraki.addEventListener("click", function () { goster(i + 1); });
  document.getElementById("tamekran").addEventListener("click", tamEkran);
  document.addEventListener("fullscreenchange", tamDegisti);
  document.addEventListener("webkitfullscreenchange", tamDegisti);

  document.addEventListener("keydown", function (e) {
    if (e.altKey || e.ctrlKey || e.metaKey) return;
    var k = e.key;
    if (k === "ArrowRight" || k === "PageDown" || k === "ArrowDown") { e.preventDefault(); goster(i + 1); }
    else if (k === "ArrowLeft" || k === "PageUp" || k === "ArrowUp") { e.preventDefault(); goster(i - 1); }
    else if (k === "Home") { e.preventDefault(); goster(0); }
    else if (k === "End") { e.preventDefault(); goster(n - 1); }
    else if ((k === "f" || k === "F") && !/^(INPUT|TEXTAREA)$/.test(e.target.tagName)) { tamEkran(); }
  });

  var x0 = null, y0 = null;
  sahne.addEventListener("touchstart", function (e) {
    if (e.touches.length !== 1) { x0 = null; return; }
    x0 = e.touches[0].clientX; y0 = e.touches[0].clientY;
  }, { passive: true });
  sahne.addEventListener("touchend", function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0, dy = e.changedTouches[0].clientY - y0;
    if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) goster(i + (dx < 0 ? 1 : -1));
    x0 = null;
  }, { passive: true });

  window.addEventListener("resize", olcekle);
  window.addEventListener("hashchange", hashten);
  olcekle();
  hashten();
})();
