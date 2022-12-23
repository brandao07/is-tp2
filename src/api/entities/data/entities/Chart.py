from data.db.db import get_all, insert, get_one
from data.entities.EntityI import EntityI


class Chart(EntityI):
    @staticmethod
    def get_one(args):
        return get_one("select c.id, c.name from charts c where c.name like %s", (args[0],))

    @staticmethod
    def get_all():
        return get_all("select c.id, c.name from charts c limit 25")

    @staticmethod
    def insert(obj):
        return insert('insert into charts (name) values (%s)', (obj.name,))

    def __init__(self, id, name):
        self.id = id
        self.name = name
