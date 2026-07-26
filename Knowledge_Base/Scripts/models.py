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

@dataclass
class SearchResult:
    id: str
    text: str
    heading: str
    page: int
    source: str
    distance: float