from db import db


def order_by_streams():
    query = """
    with
    artists as (
        select
            unnest(xpath('/spotify/regions/region/artists/artist', xml)) as artist
        from imported_documents where is_deleted = false
    ),

    artists_with_tracks as (
        select
            (xpath('/artist/@name', artist))[1]::text as artist_name,
            unnest(xpath('//track/streams/text()', artist))::text::int as n_streams
        from artists
    )

select
    artist_name,
    sum(n_streams)
from
    artists_with_tracks
    group by artist_name
    order by sum(n_streams) desc
       """

    return db.get_all(query)
