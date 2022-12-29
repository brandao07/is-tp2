import psycopg2

from utils.logger import logger


def open_connection():
    conn = None

    try:
        conn = psycopg2.connect(host='db-xml', database='is', user='is', password='is')

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


def get_all(query):
    connection = None
    cursor = None

    try:
        connection = open_connection()
        cursor = connection.cursor()

        cursor.execute(query)
        connection.commit()
        return cursor.fetchall()

    except Exception as error:
        logger(error)
        return None

    finally:
        if connection is not None:
            close_connection(connection)
            cursor.close()


def get_one(query):
    connection = None
    cursor = None

    try:
        connection = open_connection()
        cursor = connection.cursor()

        cursor.execute(query)
        connection.commit()
        return cursor.fetchone()

    except Exception as error:
        logger(error)
        return None

    finally:
        if connection is not None:
            close_connection(connection)
            cursor.close()


def execute(query):
    connection = None
    cursor = None

    try:
        connection = open_connection()
        cursor = connection.cursor()

        cursor.execute(query)
        connection.commit()
        return True

    except Exception as error:
        logger(error)
        return False

    finally:
        if connection is not None:
            close_connection(connection)
            cursor.close()


def execute_with_args(query, args):
    connection = None
    cursor = None

    try:
        connection = open_connection()
        cursor = connection.cursor()

        cursor.execute(query, args)
        connection.commit()
        return True

    except Exception as error:
        logger(error)
        return False

    finally:
        if connection is not None:
            close_connection(connection)
            cursor.close()
