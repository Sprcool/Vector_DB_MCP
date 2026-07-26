from .models import KnowledgeRecord


def deduplicate_records(
    records: list[KnowledgeRecord]
) -> list[KnowledgeRecord]:

    before = len(records)

    unique_records = {}

    for record in records:
        unique_records[record.id] = record

    after = len(unique_records)

    print(f"Removed {before - after} duplicate chunks")

    return list(unique_records.values())