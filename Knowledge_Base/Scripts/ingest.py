from config import PDF_PATH

from document_parser import load_document
from chunker import chunk_document
from chunk_mapper import build_records
from models import KnowledgeRecord


def ingest_pdf(pdf_path):

    document = load_document(pdf_path)

    chunks = chunk_document(document)

    records = build_records(chunks)

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



      

if __name__ == "__main__":
    main()