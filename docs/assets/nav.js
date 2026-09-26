/* GEMSDOE research library — progressive enhancement only.
   Everything on the site is readable and navigable with JavaScript disabled. */
(function () {
  "use strict";

  /* ------------------------------------------------ mark current nav item */
  function markCurrent() {
    var here = location.pathname.replace(/\/+$/, "") || "/";
    var links = document.querySelectorAll("header.site nav a");
    for (var i = 0; i < links.length; i++) {
      var a = links[i];
      var href = a.getAttribute("href") || "";
      if (href.charAt(0) === "#" || href.indexOf("http") === 0) continue;
      var clean = href.replace(/\.\.\//g, "").replace(/^\//, "");
      if (!clean) continue;
      if (here === clean || here.indexOf("/" + clean) === here.length - clean.length - 1) {
        a.setAttribute("aria-current", "page");
      }
    }
  }

  /* --------------------------------------------------------- build the TOC */
  function buildToc() {
    var slot = document.querySelector(".toc");
    if (!slot) return;
    var main = document.getElementById("main");
    if (!main) return;
    var heads = main.querySelectorAll("h2[id]");
    if (heads.length < 3) { slot.parentNode.classList.remove("has-toc"); slot.remove(); return; }
    var h = document.createElement("h2");
    h.textContent = "On this page";
    slot.appendChild(h);
    var ol = document.createElement("ol");
    for (var i = 0; i < heads.length; i++) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = "#" + heads[i].id;
      a.textContent = heads[i].textContent.replace(/§/g, "§");
      li.appendChild(a);
      ol.appendChild(li);
    }
    slot.appendChild(ol);
  }

  /* ------------------------------------------------- client-side filtering */
  function norm(s) { return (s || "").toLowerCase(); }

  function applyFilter(input) {
    var target = document.querySelector(input.getAttribute("data-filter"));
    if (!target) return;
    var q = norm(input.value).trim();
    var mode = input.getAttribute("data-filter-mode") || "rows";
    var items = mode === "rows"
      ? target.querySelectorAll("tbody tr")
      : target.querySelectorAll("[data-filter-item]");
    var shown = 0;
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      var text = norm(item.textContent);
      var chips = norm(item.getAttribute("data-tags") || "");
      var match = !q || text.indexOf(q) !== -1 || chips.indexOf(q) !== -1;
      item.style.display = match ? "" : "none";
      if (match) shown++;
    }
    var out = document.querySelector(input.getAttribute("data-filter-count"));
    if (out) out.textContent = shown + " of " + items.length;
  }

  function wireFilters() {
    var inputs = document.querySelectorAll("input[data-filter], select[data-filter]");
    for (var i = 0; i < inputs.length; i++) {
      (function (input) {
        input.addEventListener("input", function () { applyFilter(input); });
        input.addEventListener("change", function () { applyFilter(input); });
      })(inputs[i]);
    }
  }

  /* --------------------------------------------------- status chip legend */
  function countChips() {
    var out = document.querySelector("[data-chip-count]");
    if (!out) return;
    var tally = {};
    var chips = document.querySelectorAll("main .chip");
    for (var i = 0; i < chips.length; i++) {
      var key = chips[i].className.replace("chip", "").trim() || "other";
      var label = norm(chips[i].textContent);
      tally[label] = (tally[label] || 0) + 1;
    }
    var parts = [];
    for (var k in tally) if (Object.prototype.hasOwnProperty.call(tally, k)) parts.push(k + ": " + tally[k]);
    out.textContent = parts.join(" · ");
  }

  function init() {
    markCurrent();
    buildToc();
    wireFilters();
    countChips();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
