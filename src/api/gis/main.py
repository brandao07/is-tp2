import sys

from flask import Flask, jsonify, request
from flask_cors import CORS

from data import db
from data.Serializable import Serializable

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 9000

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/api/markers', methods=['GET'])
def get_markers():
    args = request.args
    ne_lat = float(args.get("ne_lat"))
    ne_lon = float(args.get("ne_lon"))
    sw_lat = float(args.get("sw_lat"))
    sw_lon = float(args.get("sw_lon"))

    if db.get_all(ne_lat, ne_lon, sw_lat, sw_lon) is not None:
        return jsonify({"Markers": [Serializable.marker(x) for x in db.get_all(ne_lat, ne_lon, sw_lat, sw_lon)]}), 200

    return jsonify({"Markers": []}), 418


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
