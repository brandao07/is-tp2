from db import db


def order_by_streams():
    query = """
    select
    artist_name,
    sum(n_streams)
    from (
    select
        artist_name::text,
        unnest(xpath('tracks/track/streams/text()', artist_xpath))::text::int as n_streams
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
    order by sum(n_streams) desc
       """

    return db.get_all(query)