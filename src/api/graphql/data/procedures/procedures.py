from data.db import db


class Procedures:

    @staticmethod
    def find_by_region(region_name: str):
        query = """
            select t.id, t.title, t.url, t.streams, t.rank, t.date, t.trend, a.name, r.name
        from tracks t
            inner join regions r on r.id = t.regions_id
            inner join artists a on a.id = t.artists_id
        where r.name = %s
            and not t.is_deleted
            and not r.is_deleted
            and not a.is_deleted
        """
        return db.get_all(query, (region_name,))

    @staticmethod
    def find_by_region_artist(region_name: str, artist_name: str):
        query = """
        select t.id, t.title, t.url, t.streams, t.rank, t.date, t.trend, a.name, r.name
        from tracks t
            inner join regions r on r.id = t.regions_id
            inner join artists a on a.id = t.artists_id
        where r.name = %s
            and a.name = %s
            and not t.is_deleted
            and not r.is_deleted
            and not a.is_deleted
        """
        return db.get_all(query, (region_name, artist_name))

    @staticmethod
    def artist_streams():
        query = """
            select a.name, sum(t.streams::int)
            from tracks t
                inner join artists a on a.id = t.artists_id
            where not t.is_deleted
                and not a.is_deleted
            group by a.name
            order by sum(t.streams::int) desc
          """
        return db.get_all(query, ())

    @staticmethod
    def artist_tracks():
        query = """
            select a.name, count(*)
            from tracks t
                inner join artists a on a.id = t.artists_id
            where not t.is_deleted
                and not a.is_deleted
            group by a.name
            order by sum(t.streams::int) desc
            """
        return db.get_all(query, ())
