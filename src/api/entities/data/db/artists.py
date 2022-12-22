from data.db.connection import close_db_connection, open_db_connection

from data.entities.artist import Artist

from logger import log_error


def get_artists():
    connection = None
    cursor = None

    try:
        connection = open_db_connection()
        cursor = connection.cursor()

        cursor.execute("select a.id, a.name from artists a limit 25")
        connection.commit()
        return cursor.fetchall()

    except Exception as error:
        log_error(error)
        return None

    finally:
        if connection is not None:
            close_db_connection(connection)
            cursor.close()


def create_artist(artist: Artist):
    connection = None
    cursor = None

    try:
        connection = open_db_connection()
        cursor = connection.cursor()

        cursor.execute('insert into artists (name) values (%s)', (artist.name, ))
        connection.commit()
        return True

    except Exception as error:
        log_error(error)
        return False

    finally:
        if connection is not None:
            close_db_connection(connection)
            cursor.close()
