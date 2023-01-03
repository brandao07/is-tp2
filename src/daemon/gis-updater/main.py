import sys
import time
import requests
import json

from Serializable import Serializable

POLLING_FREQ = int(sys.argv[1]) if len(sys.argv) >= 2 else 60
ENTITIES_PER_ITERATION = int(sys.argv[2]) if len(sys.argv) >= 3 else 10


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
        # TODO: Fazer um GET a entities API a procura dos paises sem coordenadas
        # TODO: Apos o GET adicionar coordenadas com o API que estamos a usar no importer
        # TODO: Apos inserir as coordenadas mandar de volta para o entities API que vai adicionar na bd

        # TODO: FAZER um get para populate regions
        r = requests.get("http://api-entities:8080/api/regions/pending/")
        data = r.json()
        # PODE NAO FUNCIONAR
        regions = data["Regions"]
        for x in regions:
            coords = generate_coords(x["name"])
            # TODO: Fazer uma POST request a API entities a mandar o x (region) e as coords[0] = lat coords[1] = lon
            url = 'http://api-entities:8080/api/regions/pending/'
            obj = (x["name"], coords[0], coords[1])
            data = Serializable.region(obj)
            headers = {'Content-Type': 'application/json'}
            requests.post(url, data=json.dumps(data), headers=headers)

        time.sleep(POLLING_FREQ)
