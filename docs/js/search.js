(function () {
  // Static index of major sections. Rebuilt by hand when pages change —
  // there's no build step in this static site, so keep entries short and current.
  var INDEX = [
    { title: "Overview", page: "Home", href: "index.html" },
    { title: "Why RAG?", page: "Home", href: "index.html#why-rag" },
    { title: "High-level RAG flow", page: "Home", href: "index.html#flow" },
    { title: "Technology stack", page: "Home", href: "index.html#stack" },

    { title: "End-to-End RAG Architecture", page: "Architecture", href: "architecture.html" },
    { title: "Sequence diagram", page: "Architecture", href: "architecture.html#sequence" },
    { title: "Data model", page: "Architecture", href: "architecture.html#model" },
    { title: "Design principles", page: "Architecture", href: "architecture.html#principles" },
    { title: "Performance & design characteristics", page: "Architecture", href: "architecture.html#performance" },
    { title: "Project structure", page: "Architecture", href: "architecture.html#structure" },

    { title: "01 Document Ingestion", page: "Pipeline", href: "pipeline.html#s01" },
    { title: "02 Document Parsing", page: "Pipeline", href: "pipeline.html#s02" },
    { title: "03 Semantic Chunking", page: "Pipeline", href: "pipeline.html#s03" },
    { title: "04 Metadata Mapping", page: "Pipeline", href: "pipeline.html#s04" },
    { title: "05 Deduplication", page: "Pipeline", href: "pipeline.html#s05" },
    { title: "06 Embedding Generation", page: "Pipeline", href: "pipeline.html#s06" },
    { title: "07 Vector Indexing", page: "Pipeline", href: "pipeline.html#s07" },
    { title: "08 Semantic Retrieval", page: "Pipeline", href: "pipeline.html#s08" },
    { title: "09 MCP Integration", page: "Pipeline", href: "pipeline.html#s09" },

    { title: "config.py", page: "Modules", href: "modules.html#config" },
    { title: "models.py", page: "Modules", href: "modules.html#models" },
    { title: "document_parser.py", page: "Modules", href: "modules.html#document_parser" },
    { title: "chunker.py", page: "Modules", href: "modules.html#chunker" },
    { title: "chunk_mapper.py", page: "Modules", href: "modules.html#chunk_mapper" },
    { title: "deduplicator.py", page: "Modules", href: "modules.html#deduplicator" },
    { title: "embeddings.py", page: "Modules", href: "modules.html#embeddings" },
    { title: "vector_store.py", page: "Modules", href: "modules.html#vector_store" },
    { title: "retrieval_service.py", page: "Modules", href: "modules.html#retrieval_service" },
    { title: "ingest.py", page: "Modules", href: "modules.html#ingest" },
    { title: "mcp_server.py", page: "Modules", href: "modules.html#mcp_server" },

    { title: "Prerequisites", page: "Getting Started", href: "getting-started.html#prereqs" },
    { title: "Installation steps", page: "Getting Started", href: "getting-started.html#steps" },
    { title: "Sample queries", page: "Getting Started", href: "getting-started.html#samples" },

    { title: "search_knowledge_base tool", page: "API", href: "api.html#search-tool" },
    { title: "Request parameters", page: "API", href: "api.html#params" },
    { title: "Response schema", page: "API", href: "api.html#response" },

    { title: "Roadmap", page: "Roadmap", href: "roadmap.html" }
  ];

  document.addEventListener("DOMContentLoaded", function () {
    var input = document.getElementById("search-input");
    var results = document.getElementById("search-results");
    if (!input || !results) return;

    function render(items) {
      if (!items.length) {
        results.innerHTML = '<div class="search-empty">No matches.</div>';
        results.classList.add("open");
        return;
      }
      results.innerHTML = items
        .slice(0, 10)
        .map(function (item) {
          return (
            '<a href="' + item.href + '">' +
            item.title +
            '<span class="p">' + item.page + "</span></a>"
          );
        })
        .join("");
      results.classList.add("open");
    }

    input.addEventListener("input", function () {
      var q = input.value.trim().toLowerCase();
      if (!q) {
        results.classList.remove("open");
        return;
      }
      var matches = INDEX.filter(function (item) {
        return item.title.toLowerCase().indexOf(q) !== -1 || item.page.toLowerCase().indexOf(q) !== -1;
      });
      render(matches);
    });

    input.addEventListener("focus", function () {
      if (input.value.trim()) results.classList.add("open");
    });

    document.addEventListener("click", function (e) {
      if (!results.contains(e.target) && e.target !== input) {
        results.classList.remove("open");
      }
    });

    document.addEventListener("keydown", function (e) {
      if ((e.key === "/" || (e.ctrlKey && e.key === "k")) && document.activeElement !== input) {
        e.preventDefault();
        input.focus();
      }
      if (e.key === "Escape") {
        results.classList.remove("open");
        input.blur();
      }
    });
  });
})();
