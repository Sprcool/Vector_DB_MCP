(function () {
  var PAGES = [
    { href: "index.html", title: "Overview" },
    { href: "architecture.html", title: "End-to-End RAG Architecture" },
    { href: "pipeline.html", title: "Pipeline Stages" },
    { href: "modules.html", title: "Module Reference" },
    { href: "getting-started.html", title: "Getting Started" },
    { href: "api.html", title: "API Reference" },
    { href: "roadmap.html", title: "Roadmap" }
  ];

  function currentPage() {
    return document.body.getAttribute("data-page") || "index.html";
  }

  function markActive() {
    var page = currentPage();
    var links = document.querySelectorAll(".sidebar a[href]");
    links.forEach(function (a) {
      var href = a.getAttribute("href").split("#")[0];
      if (href === page) a.classList.add("active");
    });
  }

  function buildPageNav() {
    var mount = document.getElementById("page-nav");
    if (!mount) return;
    var page = currentPage();
    var idx = PAGES.findIndex(function (p) { return p.href === page; });
    if (idx === -1) return;
    var prev = PAGES[idx - 1];
    var next = PAGES[idx + 1];
    var html = "";
    html += prev
      ? '<a class="prev" href="' + prev.href + '"><span class="lbl">← Previous</span><span class="ttl">' + prev.title + "</span></a>"
      : "<span></span>";
    html += next
      ? '<a class="next" href="' + next.href + '"><span class="lbl">Next →</span><span class="ttl">' + next.title + "</span></a>"
      : "<span></span>";
    mount.innerHTML = html;
  }

  function setupMobileToggle() {
    var btn = document.getElementById("menu-toggle");
    var sidebar = document.getElementById("sidebar");
    if (!btn || !sidebar) return;
    btn.addEventListener("click", function () {
      sidebar.classList.toggle("open");
    });
    document.addEventListener("click", function (e) {
      if (!sidebar.classList.contains("open")) return;
      if (sidebar.contains(e.target) || btn.contains(e.target)) return;
      sidebar.classList.remove("open");
    });
  }

  // Highlights the sidebar sub-link for the section currently in view.
  // Sidebar links point to "page.html#id" (they're shared across every page),
  // so only links whose file part matches the current page are eligible.
  function setupScrollSpy() {
    var page = currentPage();
    var subLinks = Array.prototype.filter.call(
      document.querySelectorAll(".sidebar li.sub a[href*='#']"),
      function (a) {
        var href = a.getAttribute("href");
        var file = href.split("#")[0];
        return file === "" || file === page;
      }
    );
    if (!subLinks.length || !("IntersectionObserver" in window)) return;

    var map = {};
    subLinks.forEach(function (a) {
      var id = a.getAttribute("href").split("#")[1];
      var el = document.getElementById(id);
      if (el) map[id] = a;
    });

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          var link = map[entry.target.id];
          if (!link) return;
          if (entry.isIntersecting) {
            subLinks.forEach(function (l) { l.classList.remove("active"); });
            link.classList.add("active");
          }
        });
      },
      { rootMargin: "-30% 0px -60% 0px" }
    );
    Object.keys(map).forEach(function (id) {
      observer.observe(document.getElementById(id));
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    markActive();
    setupScrollSpy();
    setupMobileToggle();
    buildPageNav();
  });
})();
