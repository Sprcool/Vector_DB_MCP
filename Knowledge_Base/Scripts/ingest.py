from .config import PDF_PATH
from .embeddings import EmbeddingService
from .vector_store import VectorStore
from document_parser import load_document
from .chunker import chunk_document
from .chunk_mapper import build_records
from .models import KnowledgeRecord
from collections import Counter
from .deduplicator import deduplicate_records
from .retrieval_service import RetrievalService


def ingest_pdf(pdf_path):

    document = load_document(pdf_path)

    chunks = chunk_document(document)

    records = build_records(chunks)

    records = deduplicate_records(records)

    print(len(records))

    return records


# def main():

#     records = ingest_pdf(PDF_PATH)

#     print(f"Records created: {len(records)}")

#     print(records[0])

def main():

    records = ingest_pdf(PDF_PATH)

    print(f"Total Records : {len(records)}")
    print("-" * 80)

    ids = [record.id for record in records]
    print(f"Total IDs    : {len(ids)}")
    print(f"Unique IDs   : {len(set(ids))}")  
    longest = max(records, key=lambda r: len(r.text))

    print(len(longest.text))
    print(longest.heading)
    for i, record in enumerate(records[:5], start=1):
        print(f"Record {i}")
        print(record)
        print("-" * 80)

    # Create the service
    embedding_service = EmbeddingService()

    # Generate embeddings
    embedded_records = embedding_service.embed(records)

    print(f"Knowledge Records : {len(records)}")
    print(f"Embedded Records : {len(embedded_records)}")
    print(embedded_records[0])
    print(len(embedded_records[0].embedding))

    record = embedded_records[0]

    print(record.record.id)
    print(record.record.heading)
    print(record.record.page)
    print(record.record.source)

    print(type(embedded_records[0].embedding))

    print(embedded_records[0].embedding[:10])

    lengths = {len(record.embedding) for record in embedded_records}

    print(lengths)

    for original, embedded in zip(records, embedded_records):
        assert original.id == embedded.record.id

        print("All IDs Match")

    # print(f"Encoding {len(texts)} texts...")

    print(embedding_service.model)

    ids = [record.record.id for record in embedded_records]

    print(f"Total IDs  : {len(ids)}")
    print(f"Unique IDs : {len(set(ids))}")

    # -----------------------------
    # Phase 3 : Vector Database
    # -----------------------------

    vector_store = VectorStore()

    vector_store.store(embedded_records)

    print("✓ Vector DB populated successfully.")

    print(f"Vectors Stored : {vector_store.count()}")  

    def count(self) -> int:
        return self.collection.count()

    print(vector_store.count())

    embedding_service = EmbeddingService()
    vector_store = VectorStore()

    retrieval_service = RetrievalService(
        embedding_service,
        vector_store
    )

    results = retrieval_service.search(
        "What is Azure Data Factory?"
    )

    for result in results:
        print("-" * 80)
        print(f"Heading : {result.heading}")
        print(f"Page    : {result.page}")
        print(f"Distance: {result.distance:.3f}")
        print(result.text)

if __name__ == "__main__":
    main()