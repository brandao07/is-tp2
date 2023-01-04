import sys

from flask import Flask, jsonify, request
from flask_cors import CORS

from data.entities.Artist import Artist
from data.entities.Region import Region
from data.db.Serializable import Serializable
from data.entities.Track import Track

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 9000

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


# TODO O DAEMON GIS É QUE ADICIONA AS COORDENADAS

@app.route('/api/artists/', methods=['GET'])
def get_artists():
    return jsonify({"Artists": [Serializable.artist(x) for x in Artist.get_all()]}), 200


@app.route('/api/artists/', methods=['POST'])
def create_artist():
    data = request.get_json()

    if Artist.insert(Artist(name=data['name'], id=None)):
        return "artist created successfully!", 201

    return "error while creating artist", 500


@app.route('/api/artists/<id>', methods=['DELETE'])
def delete_artist(id):
    if Artist.delete(id):
        return "artist deleted successfully!", 201

    return "error while deleting artist", 500


@app.route('/api/artists/<id>', methods=['PUT'])
def update_artist(id):
    data = request.get_json()
    if Artist.update(Artist(name=data['name'], id=id)):
        return "artist updated successfully!", 201

    return "error while updating artist", 500


@app.route('/api/regions/', methods=['GET'])
def get_regions():
    return jsonify({"Regions": [Serializable.region(x) for x in Region.get_all()]}), 200


@app.route('/api/regions/', methods=['POST'])
def create_region():
    data = request.get_json()

    if Region.insert(Region(name=data['name'], id=None, lat=data['lat'], lon=data['lon'], geom=None)):
        return "region created successfully!", 201

    return "error while creating region", 500


@app.route('/api/regions/pending/', methods=['GET'])
def show_pending():
    return jsonify({"Regions": [Serializable.pending_region(x) for x in Region.get_pending()]}), 200


@app.route('/api/regions/pending/', methods=['POST'])
def add_coords():
    data = request.get_json()
    if Region.add_coords(Region(name=data['name'], id=None, lat=data['lat'], lon=data['lon'], geom=None)):
        return "coords added successfully!", 201
    return "error while adding coords", 500


@app.route('/api/regions/<id>', methods=['DELETE'])
def delete_region(id):
    if Region.delete(id):
        return "region deleted successfully!", 201

    return "error while deleting region", 500


@app.route('/api/regions/<id>', methods=["PUT"])
def update_region(id):
    data = request.get_json()
    if Region.update(Region(name=data['name'], id=id, geom=data['geom'], lat=None, lon=None)):
        return "region updated successfully!", 201

    return "error while updating region", 500


@app.route('/api/tracks/', methods=['GET'])
def get_tracks():
    return jsonify({"Tracks": [Serializable.track(x) for x in Track.get_all()]}), 200


@app.route('/api/tracks/', methods=['POST'])
def create_tracks():
    data = request.get_json()

    if Track.insert(Track(title=data['title'],
                          url=data['url'],
                          streams=data['streams'],
                          date=data['date'],
                          rank=data['rank'],
                          trend=data['trend'],
                          artists_id=Artist.get_one_by_name(data['artist_name'])[0],
                          regions_id=Region.get_one_by_name(data['region_name'])[0],
                          id=None)):
        return "track created successfully!", 201

    return "error while creating track", 500


@app.route('/api/tracks/<id>', methods=['DELETE'])
def delete_track(id):
    if Track.delete(id):
        return "track deleted successfully!", 201

    return "error while deleting track", 500


@app.route('/api/tracks/<id>', methods=['PUT'])
def update_track(id):
    data = request.get_json()

    if Artist.get_one_by_name(data['artist_name']) is None:
        artists_id = ""
    else:
        artists_id = Artist.get_one_by_name(data['artist_name'])[0]

    if Region.get_one_by_name(data['region_name']) is None:
        regions_id = ""
    else:
        regions_id = Region.get_one_by_name(data['region_name'])[0]

    if Track.update(Track(id=id,
                          title=data['title'],
                          trend=data['trend'],
                          rank=data['rank'],
                          url=data['url'],
                          date=data['date'],
                          streams=data['streams'],
                          artists_id=artists_id,
                          regions_id=regions_id
                          )
                    ):
        return "track updated successfully!", 201

    return "error while updating track", 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
