from data.db.db import get_all, execute, get_one
from data.entities.EntityI import EntityI


class Artist(EntityI):
    @staticmethod
    def delete(id):
        return execute("update artists set is_deleted = true where id = %s", (id, ))

    @staticmethod
    def get_one_by_name(name):
        return get_one("select id, name from artists where name like %s and is_deleted = false", (name,))

    @staticmethod
    def get_by_id(id):
        return get_one("select id, name from artists where id = %s and is_deleted = false", (id,))

    @staticmethod
    def get_all():
        return get_all("select id, name from artists where is_deleted = false limit 25")

    @staticmethod
    def insert(obj):
        return execute('insert into artists (name) values (%s)', (obj.name, ))

    @staticmethod
    def update(obj):
        old = Artist.get_by_id(obj.id)
        if obj.name == "":
            obj.name = old[1]
        return execute('update artists set name = %s where id = %s', (obj.name, obj.id))

    def __init__(self, id, name):
        self.id = id
        self.name = name
