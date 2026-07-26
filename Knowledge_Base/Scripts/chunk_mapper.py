import hashlib

from models import KnowledgeRecord


def get_text(chunk):
    return chunk.text


def get_heading(chunk):
    headings = chunk.meta.headings

    if not headings:
        return ""

    return " > ".join(headings)


def get_page_number(chunk):

    if not chunk.meta.doc_items:
        return 0

    first_item = chunk.meta.doc_items[0]

    if not first_item.prov:
        return 0

    return first_item.prov[0].page_no


def get_source(chunk):
    return chunk.meta.origin.filename


def generate_chunk_id(text, heading, page, source):

    value = f"{source}|{page}|{heading}|{text}"

    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def build_record(chunk):

    text = get_text(chunk)
    heading = get_heading(chunk)
    page = get_page_number(chunk)
    source = get_source(chunk)

    return KnowledgeRecord(
        id=generate_chunk_id(text, heading, page, source),
        text=text,
        heading=heading,
        page=page,
        source=source,
    )


def build_records(chunks):

    return [build_record(chunk) for chunk in chunks]