from db import db


def find_by_region(file_name: str, region: str):
    query = f"select unnest(xpath('/spotify/regions/region[@name='{region}']', xml)) " \
            f"from imported_documents where file_name like {file_name} and is_deleted = false"

    return db.get_all(query)
