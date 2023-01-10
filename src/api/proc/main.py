import sys
import xmlrpc.client

from flask import Flask, request
from flask_cors import CORS

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
    # TODO: Serialize data
    return data


@app.route("/api/regions/artists", method=['GET'])
def find_region_artist():
    args = request.args
    data = server.find_by_artist_region(args.get("region_name"), args.get("artist_name"))
    # TODO: Serialize data
    return data


@app.route("/api/streams", method=['GET'])
def order_streams():
    data = server.order_by_streams()
    # TODO: Serialize data
    return data


@app.route("/api/dates/artists", methods=['GET'])
def group_date_artist():
    data = server.group_by_date_artist()
    # TODO: Serialize data
    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
