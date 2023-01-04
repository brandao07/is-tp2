from data.db.db import get_all, get_one, execute
from data.entities.EntityI import EntityI


class Region(EntityI):
    @staticmethod
    def get_by_id(id):
        return get_one("select id, name, geom from regions where id = %s and is_deleted = false", (id,))

    @staticmethod
    def update(obj):
        old = Region.get_by_id(obj.id)
        if obj.name == "":
            obj.name = old[1]
        if obj.geom == "":
            obj.geom = old[2]
        return execute('update regions set name = %s, geom = %s where id = %s', (obj.name, obj.geom, obj.id))


    @staticmethod
    def delete(id):
        return execute("update regions set is_deleted = true where id = %s", (id,))

    @staticmethod
    def get_all():
        return get_all("select id, name, geom from regions where is_deleted = false")

    @staticmethod
    def get_pending():
        return get_all("select name from regions where geom is null and is_deleted = false")

    @staticmethod
    def add_coords(obj):
        return execute('update regions set geom = ST_SetSRID(ST_MakePoint(%s, %s),4326) where name like %s',
                       (float(obj.lat), float(obj.lon), obj.name))

    @staticmethod
    def insert(obj):
        return execute('insert into regions (name, geom) values (%s, ST_SetSRID(ST_MakePoint(%s, %s),4326))',
                       (obj.name, float(obj.lat), float(obj.lon)))

    @staticmethod
    def get_one_by_name(name):
        return get_one("select id, name, geom from regions where name like %s and is_deleted = false", (name,))

    def __init__(self, id, name, geom, lat, lon):
        self.id = id
        self.name = name
        self.geom = geom
        self.lat = lat
        self.lon = lon
