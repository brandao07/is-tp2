from data.db.db import get_all, insert, get_one, delete
from data.entities.EntityI import EntityI


class Chart(EntityI):
    @staticmethod
    def delete(id):
        return delete("update charts set is_deleted = true where id = %s", (id, ))

    @staticmethod
    def get_one(args):
        return get_one("select c.id, c.name from charts c where c.name like %s and is_deleted = false", (args[0],))

    @staticmethod
    def get_all():
        return get_all("select c.id, c.name from charts c where is_deleted = false limit 25")

    @staticmethod
    def insert(obj):
        return insert('insert into charts (name) values (%s)', (obj.name,))

    def __init__(self, id, name):
        self.id = id
        self.name = name
