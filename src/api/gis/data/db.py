import psycopg2

from utils.logger import logger


def open_connection():
    conn = None

    try:
        conn = psycopg2.connect(host='db-rel', database='is', user='is', password='is')

    except (Exception, psycopg2.DatabaseError) as error:
        logger(error)

    finally:
        if conn is not None:
            return conn


def close_connection(conn):
    try:
        conn.close()

    except Exception as error:
        logger(error)
        return False

    finally:
        return True


def get_all(ne_lat, ne_lon, sw_lat, sw_lon):
    connection = None
    cursor = None

    try:
        connection = open_connection()
        cursor = connection.cursor()
        query = """
            select distinct 
            t.id, t.title, t.date, t.streams, t.rank, t.url, t.trend, r.name, a.name, ST_X(r.geom), ST_Y(r.geom)
            from tracks t
                inner join regions r on r.id = t.regions_id
                inner join artists a on a.id = t.artists_id
            where t.rank = 1 and t.date = '2017-01-01' and st_within(r.geom, st_makeenvelope(%s, %s, %s, %s, 4326))
            """
        cursor.execute(query, (ne_lat, ne_lon, sw_lat, sw_lon))
        connection.commit()
        return cursor.fetchall()

    except Exception as error:
        logger(error)
        return None

    finally:
        if connection is not None:
            close_connection(connection)
            cursor.close()
