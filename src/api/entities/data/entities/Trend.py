from data.db.db import get_all, insert, get_one, delete
from data.entities.EntityI import EntityI


class Trend(EntityI):
    @staticmethod
    def delete(id):
        return delete("update trends set is_deleted = true where id = %s", (id, ))

    @staticmethod
    def get_all():
        return get_all("select t.id, t.name from trends t where is_deleted = false limit 25")

    @staticmethod
    def insert(obj):
        return insert('insert into trends (name) values (%s)', (obj.name,))

    @staticmethod
    def get_one(args):
        return get_one("select t.id, t.name from trends t where t.name like %s and is_deleted = false", (args[0],))

    def __init__(self, id, name):
        self.id = id
        self.name = name
