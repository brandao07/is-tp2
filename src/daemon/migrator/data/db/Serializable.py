class Serializable:

    @staticmethod
    def artist(row):
        return {
            "name": row[0]
        }

    @staticmethod
    def region(row):
        return {
            "name": row[0],
            "lat": row[1],
            "lon": row[2]
        }

    @staticmethod
    def track(row):
        return {
            "title": row[0],
            "url": row[1],
            "streams": row[2],
            "rank": row[3],
            "date": row[4],
            "trend": row[5],
            "artist_name": row[6],
            "region_name": row[7]
        }
