import sys

from flask import Flask, jsonify
from flask_cors import CORS

from data import db
from data.Serializable import Serializable

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 9000

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/api/markers/', methods=['GET'])
def get_markers():
    return jsonify({"Markers": [Serializable.marker(x) for x in db.get_all()]}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
