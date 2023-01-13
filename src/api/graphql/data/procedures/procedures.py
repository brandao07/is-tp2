from data.db import db


class Procedures:

    @staticmethod
    def find_by_region(region_name: str):
        query = """
        
        """
        return db.get_all(query, (region_name,))

    @staticmethod
    def find_by_region_artist(region_name: str, artist_name: str):
        query = """

        """
        return db.get_all(query, (region_name, artist_name))

    @staticmethod
    def artist_streams():
        query = """

          """
        return db.get_all(query, ())

    @staticmethod
    def artist_tracks():
        query = """

            """
        return db.get_all(query, ())
