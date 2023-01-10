import sys
import xmlrpc.client

from flask import Flask, request, jsonify
from flask_cors import CORS

from Serializable import Serializable

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 9000

print("connecting to server...")
server = xmlrpc.client.ServerProxy("http://rpc-server:9000")

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route("/api/regions", methods=['GET'])
def find_region():
    args = request.args
    data = server.find_by_region(args.get("region_name"))
    return jsonify({"Info": [Serializable.find_by_region(x) for x in data]}), 200


@app.route("/api/regions/artists", methods=['GET'])
def find_region_artist():
    args = request.args
    data = server.find_by_artist_region(args.get("region_name"), args.get("artist_name"))
    return jsonify({"Info": [Serializable.find_by_region(x) for x in data]}), 200


@app.route("/api/streams", methods=['GET'])
def order_streams():
    data = server.order_by_streams()
    return jsonify({"Info": [Serializable.artist_streams(x) for x in data]}), 200


@app.route("/api/tracks/artists", methods=['GET'])
def group_date_artist():
    data = server.group_by_track_artist()
    return jsonify({"Info": [Serializable.artist_tracks(x) for x in data]}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
