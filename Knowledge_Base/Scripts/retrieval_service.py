from .embeddings import EmbeddingService
from .vector_store import VectorStore
from .models import SearchResult

class RetrievalService:

    def __init__(
        self,
        embedding_service: EmbeddingService,
        vector_store: VectorStore
    ):
        self.embedding_service = embedding_service
        self.vector_store = vector_store

    def search(
        self,
        question: str,
        top_k: int = 5
    ) -> list[SearchResult]:
        """
        Performs semantic search on the knowledge base.

        Args:
            question: User's natural language query.
            top_k: Number of matching documents to return.

        Returns:
            A list of SearchResult objects.
        """
        query_embedding = self.embedding_service.embed_query(question)

        results = self.vector_store.search(
            query_embedding,
            top_k
        )

        return results
