from data.db.db import get_all, insert, delete
from data.entities.EntityI import EntityI


class Track(EntityI):
    @staticmethod
    def delete(id):
        return delete("update tracks set is_deleted = true where id = %s", (id,))

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
        return insert('insert into tracks (title, url, streams, rank,date,trend,artists_id, regions_id) '
                      'values (%s, %s, %s, %s, %s, %s, %s, %s)',
                      (obj.title, obj.url, obj.streams, obj.rank, obj.date, obj.trend, obj.artists_id, obj.regions_id))

    @staticmethod
    def get_one(args):
        pass

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
