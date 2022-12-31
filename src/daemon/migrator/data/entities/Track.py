import json

from data.db.Serializable import Serializable
from data.db.db import get_all
from data.entities.EntityI import EntityI
import requests


class Track(EntityI):

    @staticmethod
    def get_all(id):
        query = """
        select
            unnest(xpath('/track/title/text()', tracks_xml)) as title,
            unnest(xpath('/track/url/text()', tracks_xml)) as url,
            unnest(xpath('/track/streams/text()', tracks_xml)) as streams,
            unnest(xpath('/track/rank/text()', tracks_xml))::text::int as rank,
            unnest(xpath('/track/@date', tracks_xml)) as date,
            unnest(xpath('/track/trend/text()', tracks_xml)) as trend,
            unnest(artist_name),
            unnest(region_name)
        from (select region_name region_name,
             xpath('/artist/@name', artist_xml) artist_name,
             unnest(xpath('/artist/tracks/track', artist_xml)) tracks_xml
        from (select xpath('/region/@name', region_xml)                  region_name,
                   unnest(xpath('/region/artists/artist', region_xml)) artist_xml
            from (select unnest(xpath('/spotify/regions/region', xml)) region_xml
                  from imported_documents where id = %s and is_deleted = false and is_rel = false)
                t1)
          t2)
        t3
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
