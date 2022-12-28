import sys
import xmlrpc.client

from flask import Flask
from flask_cors import CORS

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 9000

print("connecting to server...")
server = xmlrpc.client.ServerProxy("http://rpc-server:9000")

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/api/test/', methods=['GET'])
def test():
    print(server.string_length("Hello"))
    return "Hello", 200


@app.route('/api/hello/', methods=['GET'])
def hello_world():
    return "Hello World", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
