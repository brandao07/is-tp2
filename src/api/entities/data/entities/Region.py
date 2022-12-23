from data.db.db import get_all, insert, delete
from data.entities.EntityI import EntityI


class Region(EntityI):
    @staticmethod
    def delete(id):
        return delete("update regions set is_deleted = true where id = %s", (id, ))

    @staticmethod
    def get_all():
        return get_all("select r.id, r.name, r.geom from regions r where is_deleted = false limit 25")

    @staticmethod
    def insert(obj):
        return insert('insert into regions (name, geom) values (%s, ST_SetSRID(ST_MakePoint(%s, %s),4326))',
                      (obj.name, float(obj.lat), float(obj.lon)))

    @staticmethod
    def get_one(args):
        pass

    def __init__(self, id, name, geom, lat, lon):
        self.id = id
        self.name = name
        self.geom = geom
        self.lat = lat
        self.lon = lon
