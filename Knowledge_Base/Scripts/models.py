from dataclasses import dataclass


from dataclasses import dataclass

@dataclass
class KnowledgeRecord:
    id: str
    text: str
    heading: str
    page: int
    source: str

@dataclass
class EmbeddedKnowledgeRecord:
    record: KnowledgeRecord
    embedding: list[float]