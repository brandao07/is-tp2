from db import db


def find_by_artist_region(file_name: str, region: str, artist: str):
    query = f"select unnest(xpath('/spotify/regions/region[@name='{region}']/artists/artist[@name='{artist}']', xml))" \
            f" from " \
            f"imported_documents " \
            f"where file_name like {file_name} and is_deleted = false"

    return db.get_all(query)
