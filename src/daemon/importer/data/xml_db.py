from lxml import etree

from data import db


def transfer_file_imported(src: str, file_name: str):
    xml_file = etree.parse(src)
    s = etree.tostring(xml_file, encoding="utf8", method="xml").decode()

    return db.execute_with_args("insert into imported_documents (file_name, xml) values (%s, %s)", (file_name, s))


def transfer_file_converted(src: str, file_size: int, dst: str):
    query = f"insert into converted_documents (src, file_size, dst) values ('{src}', {file_size}, '{dst}')"
    return db.execute(query)


def get_files_converted():
    query = "select src from converted_documents"
    return db.get_all(query)
