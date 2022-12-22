import sys

from flask import Flask, jsonify, request

from data.db import artists as artists_repository
from data.entities.artist import Artist
from data.db.serializable import Serializable

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 9000

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/artists/', methods=['GET'])
def get_artists():
    artists = [Serializable.artist(x) for x in artists_repository.get_artists()]
    return jsonify({"Artists": artists}), 200


@app.route('/api/artists/', methods=['POST'])
def create_artist():
    data = request.get_json()
    artist = Artist(name=data['name'], id=None)
    if artists_repository.create_artist(artist):
        return "artist created successfully!", 201
    return "error while creating artist"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
