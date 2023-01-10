import signal
import sys
from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer

from functions.find_by_region import find_by_region
from functions.group_by_track_artist import group_by_track_artist
from functions.find_by_artist_region import find_by_artist_region
from functions.order_by_streams import order_by_streams

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 9000

if __name__ == "__main__":
    class RequestHandler(SimpleXMLRPCRequestHandler):
        rpc_paths = ('/RPC2',)


    with SimpleXMLRPCServer(('0.0.0.0', PORT), requestHandler=RequestHandler) as server:
        server.register_introspection_functions()


        def signal_handler(signum, frame):
            print("received signal")
            server.server_close()

            # perform clean up, etc. here...
            print("exiting, gracefully")
            sys.exit(0)


        # signals
        signal.signal(signal.SIGTERM, signal_handler)
        signal.signal(signal.SIGHUP, signal_handler)
        signal.signal(signal.SIGINT, signal_handler)

        # register functions
        server.register_function(find_by_region)
        server.register_function(find_by_artist_region)
        server.register_function(order_by_streams)
        server.register_function(group_by_track_artist)

        # start the server
        print(f"Starting the RPC Server in port {PORT}...")
        server.serve_forever()
