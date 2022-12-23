from data.db.db import get_all, insert, delete
from data.entities.EntityI import EntityI


class Track(EntityI):
    @staticmethod
    def delete(id):
        return delete("update tracks set is_deleted = true where id = %s", (id,))

    @staticmethod
    def get_all():
        return get_all("select t.id, t.title, t.url, t.streams, t.artist_id, t.trend_id from tracks t "
                       "where is_deleted = false limit 25")

    @staticmethod
    def insert(obj):
        return insert('insert into tracks (title, url, streams, artist_id, trend_id) '
                      'values (%s, %s, %s, %s, %s)',
                      (obj.title, obj.url, obj.streams, obj.artist_id, obj.trend_id))

    @staticmethod
    def get_one(args):
        pass

    def __init__(self, id, title, url, streams, artist_id, trend_id):
        self.id = id
        self.title = title
        self.url = url
        self.streams = streams
        self.artist_id = artist_id
        self.trend_id = trend_id
