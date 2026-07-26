import chromadb

from .config import VECTOR_DB_PATH, COLLECTION_NAME
from .models import EmbeddedKnowledgeRecord, SearchResult


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=str(VECTOR_DB_PATH)
        )

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
        )

    def store(self, embedded_records: list[EmbeddedKnowledgeRecord]):

        ids = [
            record.record.id
            for record in embedded_records
        ]

        documents = [
            record.record.text
            for record in embedded_records
        ]

        metadatas = [
            {
                "heading": record.record.heading,
                "page": record.record.page,
                "source": record.record.source,
            }
            for record in embedded_records
        ]

        embeddings = [
            record.embedding
            for record in embedded_records
        ]

        self.collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas,
            embeddings=embeddings
        )

    def reset(self):
        self.client.delete_collection(COLLECTION_NAME)
    
        self.collection = self.client.get_or_create_collection(
                name=COLLECTION_NAME
            )

    def search(
    self,
    query_embedding: list[float],
    top_k: int = 5
     ) -> list[SearchResult]:

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=["documents", "metadatas", "distances"]
        )

        search_results = []

        for index in range(len(results["ids"][0])):

            metadata = results["metadatas"][0][index]

            search_results.append(

                SearchResult(
                    id=results["ids"][0][index],
                    text=results["documents"][0][index],
                    heading=metadata["heading"],
                    page=metadata["page"],
                    source=metadata["source"],
                    distance=results["distances"][0][index]
                )

            )

        return search_results      

    def count(self) -> int:
        return self.collection.count()  