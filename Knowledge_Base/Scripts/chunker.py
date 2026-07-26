from docling.chunking import HierarchicalChunker


def chunk_document(document):

    chunker = HierarchicalChunker()

    chunks = list(chunker.chunk(document))

    return chunks