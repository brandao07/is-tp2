from db import db


def find_by_artist_region(region: str, artist: str):
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
                 unnest(xpath('/artist[@name='%s']/tracks/track', artist_xml)) tracks_xml
            from (select xpath('/region/@name', region_xml)                  region_name,
                       unnest(xpath('/region/artists/artist', region_xml)) artist_xml
                from (select unnest(xpath('/spotify/regions/region[@name='%s']', xml)) region_xml
                      from imported_documents where is_deleted = false)
                    t1)
              t2)
            t3
        """

    return db.get_all_with_args(query, (artist, region))
