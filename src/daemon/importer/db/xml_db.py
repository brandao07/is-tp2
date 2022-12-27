import db

from lxml import etree


def transfer_file_imported(src: str, file_name: str):
    xml_file = etree.parse(src)
    s = etree.tostring(xml_file, encoding="utf8", method="xml").decode()

    query = f"insert into imported_documents (file_name, xml) values ({file_name}, {s})"
    return db.execute(query)


def transfer_file_converted(src: str, file_size: int, dst: str):
    query = f"insert into converted_documents (src, file_size, dst) values ({src}, {file_size}, {dst})"
    return db.execute(query)


def get_files_converted():
    query = "select src from converted_documents"
    return db.get_all(query)

