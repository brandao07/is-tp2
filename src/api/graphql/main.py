import sys

from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Int, List, Schema

from data.procedures.procedures import Procedures

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 9000


class ArtistStreams(ObjectType):
    artist_name = String()
    streams = Int()


class ArtistAmount(ObjectType):
    artist_name = String()
    amount = Int()


class RegionTracks(ObjectType):
    id = String()
    title = String()
    url = String()
    streams = String()
    rank = Int()
    date = String()
    trend = String()
    artist_name = String()
    region_name = String()


class Query(ObjectType):
    artist_streams = List(ArtistStreams)
    artist_amount = List(ArtistAmount)
    region_tracks = List(RegionTracks, name=String(required=True))
    region_artist_tracks = List(RegionTracks, region_name=String(required=True), artist_name=String(required=True))

    def resolve_artist_streams(self, info):
        tracks = []
        for x in Procedures.artist_streams():
            track = ArtistStreams(artist_name=x[0], streams=x[1])
            tracks.append(track)
        return tracks

    def resolve_artist_amount(self, info):
        tracks = []
        for x in Procedures.artist_tracks():
            track = ArtistAmount(artist_name=x[0], amount=x[1])
            tracks.append(track)
        return tracks

    def resolve_region_tracks(self, info, name):
        tracks = []
        for x in Procedures.find_by_region(name):
            track = RegionTracks(id=x[0],
                                 title=x[1],
                                 url=x[2],
                                 streams=x[3],
                                 rank=x[4],
                                 date=x[5],
                                 trend=x[6],
                                 artist_name=x[7],
                                 region_name=x[8])
            tracks.append(track)
        return tracks

    def resolve_region_artist_tracks(self, info, region_name, artist_name):
        tracks = []
        for x in Procedures.find_by_region_artist(region_name, artist_name):
            track = RegionTracks(id=x[0],
                                 title=x[1],
                                 url=x[2],
                                 streams=x[3],
                                 rank=x[4],
                                 date=x[5],
                                 trend=x[6],
                                 artist_name=x[7],
                                 region_name=x[8])
            tracks.append(track)
        return tracks


schema = Schema(query=Query)

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
