import sys
import time

from data.db.Serializable import Serializable
from data.entities.Track import Track
from utils.logger import logger

POLLING_FREQ = int(sys.argv[1]) if len(sys.argv) >= 2 else 60

if __name__ == "__main__":

    while True:
        print("Checking updates...")
        # !TODO: 1- Execute a SELECT query to check for any changes on the table
        id = 16
        # TODO: 2- Execute a SELECT queries with xpath to retrieve the data we want to store in the relational db
        # TODO: 3- Execute INSERT queries in the destination db
        # for x in Artist.get_all(id):
        #     Artist.insert(x)
        #
        # logger(f"Artists from xml {id} were imported to the relational db")
        #
        # for x in Region.get_all(id):
        #     Region.insert(x)
        #
        # logger(f"Regions from xml {id} were imported to the relational db")

        for x in Track.get_all(id):
            print(Serializable.track(x))
            # Track.insert(x)

        logger(f"Tracks from xml {id} were imported to the relational db")

        # !TODO: 4- Make sure we store somehow in the origin database that certain records were already migrated.
        #          Change the db structure if needed.

        time.sleep(POLLING_FREQ)
