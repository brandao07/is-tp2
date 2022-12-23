from data.db.db import get_all, insert, get_one
from data.entities.EntityI import EntityI


class Trend(EntityI):
    @staticmethod
    def get_all():
        return get_all("select t.id, t.name from trends t limit 25")

    @staticmethod
    def insert(obj):
        return insert('insert into trends (name) values (%s)', (obj.name,))

    @staticmethod
    def get_one(args):
        return get_one("select t.id, t.name from trends t where t.name like %s", (args[0],))

    def __init__(self, id, name):
        self.id = id
        self.name = name
