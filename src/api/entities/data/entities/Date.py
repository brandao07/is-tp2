from data.db.db import get_all, insert
from data.entities.EntityI import EntityI


class Date(EntityI):
    @staticmethod
    def get_all():
        return get_all("select d.id, d.registered_date, d.chart_id from dates d limit 25")

    @staticmethod
    def insert(obj):
        return insert('insert into dates (registered_date, chart_id) values (%s, %s)',
                      (obj.registered_date, obj.chart_id))

    @staticmethod
    def get_one(args):
        pass

    def __init__(self, id, registered_date, chart_id):
        self.id = id
        self.registered_date = registered_date
        self.chart_id = chart_id
