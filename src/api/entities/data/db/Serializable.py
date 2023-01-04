class Serializable:

    @staticmethod
    def artist(row):
        return {
            "id": row[0],
            "name": row[1]
        }

    @staticmethod
    def region(row):
        return {
            "id": row[0],
            "name": row[1],
            "geom": row[2]
        }

    @staticmethod
    def track(row):
        return {
            "id": row[0],
            "title": row[1],
            "url": row[2],
            "streams": row[3],
            "rank": row[4],
            "date": row[5],
            "trend": row[6],
            "artist": row[7],
            "region": row[8]
        }

    @staticmethod
    def pending_region(row):
        return {
            "name": row[0]
        }
