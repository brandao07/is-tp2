import json

from data.db.Serializable import Serializable
from data.db.db import get_all
from data.entities.EntityI import EntityI
import requests


class Region(EntityI):

    @staticmethod
    def get_all(id):
        query = """
        select 
        unnest(xpath('//region/@name', xml)),
        unnest(xpath('//region/@lat', xml)),
        unnest(xpath('//region/@lon', xml))
        from imported_documents
        where id = %s and is_deleted = false and is_rel = false
        """
        args = (id,)
        return get_all(query, args)

    @staticmethod
    def insert(obj):
        url = 'http://api-entities:8080/api/regions/'
        data = Serializable.region(obj)
        headers = {'Content-Type': 'application/json'}
        requests.post(url, data=json.dumps(data), headers=headers)

        return
