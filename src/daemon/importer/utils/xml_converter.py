import csv
import requests
from xml.etree.ElementTree import SubElement, Element, ElementTree


# CONVERT FORMAT DATA TO XML
def converter(src: str, out: str):
    data = format_data(src)

    root = Element('spotify')

    regions_el = SubElement(root, 'regions')

    for idx, (region, values) in enumerate(data.items()):
        # TODO: APAGAR ISTO QUANDO O GIS-UPDATER TIVER FEITO
        coords = generate_coords(region)
        region_el = SubElement(regions_el, 'region', {
            'name': region,
            'lat': coords[0],
            'lon': coords[1]
        })

        artists_el = SubElement(region_el, 'artists')
        for artist in values['artists']:
            artist_el = SubElement(artists_el, 'artist', {
                'name': artist['name'],
            })

            tracks_el = SubElement(artist_el, 'tracks')

            for track in artist['tracks']:
                track_el = SubElement(tracks_el, 'track', {
                    'date': track['date']
                })

                SubElement(track_el, 'url').text = track['url']
                SubElement(track_el, 'title').text = track['title']
                SubElement(track_el, 'streams').text = track['streams']
                SubElement(track_el, 'rank').text = track['rank']
                SubElement(track_el, 'trend').text = track['trend']

    et = ElementTree(root)
    et.write(out)

    return 0


# FORMAT DATA FROM CSV
def format_data(src):
    with open(src) as f:
        csv_f = csv.DictReader(f)
        data = {}

        for idx, row in enumerate(csv_f):
            region = row['region']

            if region not in data:
                data[region] = {
                    'artists': []
                }

            artist_dict = next(filter(lambda artist: artist['name'] == row['artist'], data[region]['artists']), None)

            if artist_dict is None:
                artist_dict = {
                    'name': row['artist'],
                    'tracks': []
                }

                data[region]['artists'].append(artist_dict)

            artist_dict['tracks'].append({
                'url': row['url'],
                'title': row['title'],
                'streams': row['streams'],
                'rank': row['rank'],
                'trend': row['trend'],
                'date': row['date']
            })

        return data


# TODO: APAGAR ISTO QUANDO O GIS-UPDATER TIVER FEITO
# GENERATE REGION COORDS FROM API
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