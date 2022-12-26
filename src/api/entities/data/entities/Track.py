from data.db.db import get_all, execute, get_one
from data.entities.EntityI import EntityI


class Track(EntityI):
    @staticmethod
    def update(obj):
        old = Track.get_by_id(obj.id)
        if obj.title == "":
            obj.title = old[1]
        if obj.url == "":
            obj.url = old[2]
        if obj.streams == "":
            obj.streams = old[3]
        if obj.date == "":
            obj.date = old[4]
        if obj.trend == "":
            obj.trend = old[5]
        if obj.rank == 0:
            obj.rank = old[6]
        if obj.artists_id == "":
            obj.artists_id = old[7]
        if obj.regions_id == "":
            obj.regions_id = old[8]
        return execute("update tracks set title = %s, url = %s, streams = %s, date = %s, "
                       "trend = %s, rank = %s, artists_id = %s, regions_id = %s where id = %s",
                       (obj.title, obj.url, obj.streams, obj.date, obj.trend, obj.rank,
                        obj.artists_id, obj.regions_id, obj.id))

    @staticmethod
    def delete(id):
        return execute("update tracks set is_deleted = true where id = %s", (id,))

    @staticmethod
    def get_all():
        return get_all("""
                        select t.id, t.title, t.url, t.streams, t.rank, t.date, t.trend, a.name, r.name
                        from tracks t
                            inner join artists a on a.id = t.artists_id
                            inner join regions r on r.id = t.regions_id
                        where t.is_deleted = false
                        limit 25
                    """)

    @staticmethod
    def insert(obj):
        return execute('insert into tracks (title, url, streams, rank,date,trend,artists_id, regions_id) '
                       'values (%s, %s, %s, %s, %s, %s, %s, %s)',
                       (obj.title, obj.url, obj.streams, obj.rank, obj.date, obj.trend, obj.artists_id, obj.regions_id))

    @staticmethod
    def get_by_id(id):
        return get_one("select id, title, url, streams, date, trend, rank, artists_id, regions_id from tracks "
                       "where id = %s and is_deleted = false", (id,))

    def __init__(self, id, title, url, streams, rank, date, trend, artists_id, regions_id):
        self.id = id
        self.title = title
        self.url = url
        self.streams = streams
        self.trend = trend
        self.date = date
        self.rank = rank
        self.artists_id = artists_id
        self.regions_id = regions_id
