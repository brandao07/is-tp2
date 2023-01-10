from db import db


def group_by_track_artist():
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
            unnest(xpath('//track', artist)) as track
        from artists
    )

select
    artist_name,
    count(*)
from
    artists_with_tracks
group by
    artist_name
order by
    count(*) desc;
    """

    return db.get_all(query)
