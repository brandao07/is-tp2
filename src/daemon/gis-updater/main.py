import sys
import time
import requests
import json

from Serializable import Serializable

POLLING_FREQ = int(sys.argv[1]) if len(sys.argv) >= 2 else 60
ENTITIES_PER_ITERATION = int(sys.argv[2]) if len(sys.argv) >= 3 else 10


# TODO: Use ENTITIES_PER_ITERATION
def generate_coords(region: str):
    url = "https://nominatim.openstreetmap.org/"

    params = {
        'q': region,
        'limit': '1',
        'format': 'json'
    }

    r = requests.get(url=url, params=params)

    data = r.json()

    return [
        data[0]["lat"],
        data[0]["lon"]
    ]


if __name__ == "__main__":

    while True:
        print(f"Getting up to {ENTITIES_PER_ITERATION} entities without coordinates...")

        r = requests.get(f"http://api-entities:8080/api/regions/pending?amount={ENTITIES_PER_ITERATION}")
        data = r.json()
        regions = data["Regions"]
        for x in regions:
            coords = generate_coords(x["name"])
            url = 'http://api-entities:8080/api/regions/pending'
            obj = (x["name"], coords[0], coords[1])
            data = Serializable.region(obj)
            headers = {'Content-Type': 'application/json'}
            requests.post(url, data=json.dumps(data), headers=headers)

        time.sleep(POLLING_FREQ)
