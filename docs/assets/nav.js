(function () {
  var path = location.pathname.replace(/\/+$/, "") || "/";
  document.querySelectorAll("header.site nav a").forEach(function (a) {
    var href = a.getAttribute("href");
    if (!href) return;
    var normalized = href.replace(/\/index\.html$/, "/").replace(/\/+$/, "") || "/";
    if (path.endsWith(normalized.replace(/^\.\.\//, "/")) || path.endsWith(href.replace(/^\.\.\//, ""))) {
      a.setAttribute("aria-current", "page");
    }
  });
})();
