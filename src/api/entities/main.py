import sys

from flask import Flask, jsonify, request

from data.entities.Artist import Artist
from data.entities.Chart import Chart
from data.entities.Date import Date
from data.entities.Region import Region
from data.db.Serializable import Serializable
from data.entities.Track import Track
from data.entities.Trend import Trend

PORT = int(sys.argv[1]) if len(sys.argv) >= 2 else 9000

app = Flask(__name__)
app.config["DEBUG"] = True


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


@app.route('/api/charts/', methods=['GET'])
def get_charts():
    return jsonify({"Charts": [Serializable.chart(x) for x in Chart.get_all()]}), 200


@app.route('/api/charts/', methods=['POST'])
def create_chart():
    data = request.get_json()

    if Chart.insert(Chart(name=data['name'], id=None)):
        return "chart created successfully!", 201

    return "error while creating chart", 500


@app.route('/api/charts/', methods=['DELETE'])
def delete_chart(id):
    if Chart.delete(id):
        return "chart deleted successfully!", 201

    return "error while deleting chart", 500


@app.route('/api/dates/', methods=['GET'])
def get_dates():
    return jsonify({"Dates": [Serializable.date(x) for x in Date.get_all()]}), 200


@app.route('/api/dates/', methods=['POST'])
def create_date():
    data = request.get_json()

    if Date.insert(Date(registered_date=data['registered_date'],
                        chart_id=Chart.get_one((data['chart_name'],))[0],
                        id=None)):
        return "date created successfully!", 201

    return "error while creating date", 500


@app.route('/api/dates/', methods=['DELETE'])
def delete_date(id):
    if Date.delete(id):
        return "date deleted successfully!", 201

    return "error while deleting date", 500


@app.route('/api/regions/', methods=['GET'])
def get_regions():
    return jsonify({"Regions": [Serializable.region(x) for x in Region.get_all()]}), 200


@app.route('/api/regions/', methods=['POST'])
def create_region():
    data = request.get_json()

    if Region.insert(Region(name=data['name'], id=None, lat=data['lat'], lon=data['lon'], geom=None)):
        return "region created successfully!", 201

    return "error while creating region", 500


@app.route('/api/regions/', methods=['DELETE'])
def delete_region(id):
    if Region.delete(id):
        return "region deleted successfully!", 201

    return "error while deleting region", 500


@app.route('/api/trends/', methods=['GET'])
def get_trends():
    return jsonify({"Trends": [Serializable.trend(x) for x in Trend.get_all()]}), 200


@app.route('/api/trends/', methods=['POST'])
def create_trend():
    data = request.get_json()

    if Trend.insert(Trend(name=data['name'], id=None)):
        return "trend created successfully!", 201

    return "error while creating trend", 500


@app.route('/api/trends/', methods=['DELETE'])
def delete_trend(id):
    if Trend.delete(id):
        return "trend deleted successfully!", 201

    return "error while deleting trend", 500


@app.route('/api/tracks/', methods=['GET'])
def get_tracks():
    return jsonify({"Tracks": [Serializable.track(x) for x in Track.get_all()]}), 200


@app.route('/api/tracks/', methods=['POST'])
def create_tracks():
    data = request.get_json()

    if Track.insert(Track(title=data['title'],
                          url=data['url'],
                          streams=data['streams'],
                          artist_id=Artist.get_one((data['artist_name'],))[0],
                          trend_id=Trend.get_one((data['trend_name'],))[0],
                          id=None)):
        return "track created successfully!", 201

    return "error while creating track", 500


@app.route('/api/tracks/', methods=['DELETE'])
def delete_track(id):
    if Track.delete(id):
        return "track deleted successfully!", 201

    return "error while deleting track", 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
