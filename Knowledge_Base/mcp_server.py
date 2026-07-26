from dataclasses import asdict

from mcp.server.fastmcp import FastMCP

from Scripts.embeddings import EmbeddingService
from Scripts.vector_store import VectorStore
from Scripts.retrieval_service import RetrievalService


mcp = FastMCP("Knowledge Base")


embedding_service = EmbeddingService()

vector_store = VectorStore()

retrieval_service = RetrievalService(
    embedding_service,
    vector_store
)


@mcp.tool()
def search_knowledge_base(
    question: str,
    top_k: int = 5
):

    results = retrieval_service.search(
        question,
        top_k
    )

    return [
        asdict(result)
        for result in results
    ]


if __name__ == "__main__":
    mcp.run()