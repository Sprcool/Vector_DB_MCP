from pathlib import Path

KNOWLEDGE_BASE = Path(__file__).resolve().parent.parent

PDF_PATH = (
    KNOWLEDGE_BASE
    / "PDF_Source"
    / "AZURE_DATA_ENGINEERING_BROCHURE.pdf"
)

print("PDF_PATH:", PDF_PATH)
print("Exists:", PDF_PATH.exists())