import sys
import time

from data.db import db
from data.entities.Artist import Artist
from data.entities.Region import Region
from data.entities.Track import Track
from utils.logger import logger

POLLING_FREQ = int(sys.argv[1]) if len(sys.argv) >= 2 else 60


# Execute a SELECT query to check for any changes on the table
def in_queue():
    query = "select id from imported_documents where is_deleted = false and is_rel = false"
    return db.get_all(query, ())


#  Execute a SELECT queries with xpath to retrieve the data we want to store in the relational db
#  Execute INSERT queries in the destination db
def migrate(id):
    logger(f"Starting Migration for xml {id}")

    for x in Artist.get_all(id):
        Artist.insert(x)

    for x in Region.get_all(id):
        Region.insert(x)

    for x in Track.get_all(id):
        Track.insert(x)

    if set_rel(id):
        logger(f"Migration completed for xml {id}")


#  Make sure we store somehow in the origin database that certain records were already migrated.
#  Change the db structure if needed.
def set_rel(id):
    query = "update imported_documents set is_rel = true where id = %s"
    args = (id,)
    return db.execute(query, args)


if __name__ == "__main__":

    while True:
        print("Checking updates...")

        for x in in_queue():
            migrate(x[0])

        time.sleep(POLLING_FREQ)
