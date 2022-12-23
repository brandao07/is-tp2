from data.db.db import get_all, insert, get_one
from data.entities.EntityI import EntityI


class Artist(EntityI):
    @staticmethod
    def get_one(args):
        return get_one("select a.id, a.name from artists a where a.name like %s", (args[0],))

    @staticmethod
    def get_all():
        return get_all("select a.id, a.name from artists a limit 25")

    @staticmethod
    def insert(obj):
        return insert('insert into artists (name) values (%s)', (obj.name, ))

    def __init__(self, id, name):
        self.id = id
        self.name = name
