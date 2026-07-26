from sentence_transformers import SentenceTransformer

from .config import EMBEDDING_MODEL
from .models import EmbeddedKnowledgeRecord


class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def embed(self, records):
        texts = [record.text for record in records]
        vectors = self.model.encode(texts)

        embedded_records = []

        for record, vector in zip(records, vectors):
            embedded_records.append(
                EmbeddedKnowledgeRecord(
                    record=record,
                    embedding=vector.tolist()
                )
            )

        return embedded_records

    def embed_query(self, query: str) -> list[float]:

        embedding = self.model.encode(
            query,
            normalize_embeddings=True
        )

        return embedding.tolist()

    

   