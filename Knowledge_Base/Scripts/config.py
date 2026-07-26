from pathlib import Path

KNOWLEDGE_BASE = Path(__file__).resolve().parent.parent

PDF_PATH = (
    KNOWLEDGE_BASE
    / "PDF_Source"
    / "AZURE_DATA_ENGINEERING_BROCHURE.pdf"
)

EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
VECTOR_DB_PATH = KNOWLEDGE_BASE / "Vector_DB"

COLLECTION_NAME = "vector_db_mcp"