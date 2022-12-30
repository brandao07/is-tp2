import json

from data.db.Serializable import Serializable
from data.db.db import get_all
from data.entities.EntityI import EntityI
import requests


class Track(EntityI):

    @staticmethod
    def get_all(id):
        query = """
        SELECT 
        unnest(xpath('//track[url]/title/text()', xml)), 
        unnest(xpath('//track[url]/url/text()', xml)), 
        unnest(xpath('//track[url]/streams/text()', xml)), 
        unnest(xpath('//track[url]/rank/text()', xml)), 
        unnest(xpath('//track[url]/@date', xml)), 
        unnest(xpath('//track[url]/trend/text()', xml)), 
        unnest(xpath('//track[url]/../../@name', xml)), 
        unnest(xpath('//track[url]/../../../../@name', xml)) 
        from imported_documents 
        where id = %s and is_deleted = false and is_rel = false
        """
        args = (id,)
        return get_all(query, args)

    @staticmethod
    def insert(obj):
        url = 'http://api-entities:8080/api/tracks/'
        data = Serializable.track(obj)
        headers = {'Content-Type': 'application/json'}
        requests.post(url, data=json.dumps(data), headers=headers)
        return
