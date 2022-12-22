import psycopg2

from logger import log_error


def open_db_connection():
    conn = None

    try:
        print('Connecting to the PostgresSQL database...')
        conn = psycopg2.connect(host='db-rel', database='is', user='is', password='is')

    except (Exception, psycopg2.DatabaseError) as error:
        log_error(error)

    finally:
        if conn is not None:
            print("Successfully connected to the db!")
            return conn


def close_db_connection(conn) -> bool:
    try:
        print('Closing db connection...')
        conn.close()

    except Exception as error:
        log_error(error)
        return False

    finally:
        print("Successfully closed the connection to the db!")
        return True
