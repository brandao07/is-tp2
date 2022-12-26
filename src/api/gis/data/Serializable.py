class Serializable:

    @staticmethod
    def marker(row):
        return {
            "type": "feature",
            "geometry": {
                "type": 'Point',
                "coordinates": [row[9], row[10]]
            },
            "properties": {
                "id": row[0],
                "title": row[1],
                "date": row[2],
                "streams": row[3],
                "rank": row[4],
                "url": row[5],
                "trend": row[6],
                "country": row[7],
                "artist": row[8]
            }
        }
