from db import db


def group_by_date_region():
    query = """
    select
    artist_name,
    count(*)
    from (
    select
        artist_name::text,
        unnest(xpath('tracks/track', artist_xpath))
    from (
        select
            artist_xpath,
             unnest(xpath('@name', artist_xpath)) as artist_name
          from (
            select
                unnest(xpath('/spotify/regions/region/artists/artist', xml)) as artist_xpath
            from imported_documents where is_deleted = false) as t
          ) as t2
    ) as t3
    group by artist_name
    order by count(*) desc
    """

    return db.get_all(query)
