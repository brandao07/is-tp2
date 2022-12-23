class Serializable:

    @staticmethod
    def artist(row):
        return {
            "id": row[0],
            "name": row[1]
        }

    @staticmethod
    def chart(row):
        return {
            "id": row[0],
            "name": row[1]
        }

    @staticmethod
    def date(row):
        return {
            "id": row[0],
            "registered_date": row[1],
            "chart_id": row[2]
        }

    @staticmethod
    def region(row):
        return {
            "id": row[0],
            "name": row[1],
            "geom": row[2]
        }

    @staticmethod
    def trend(row):
        return {
            "id": row[0],
            "name": row[1]
        }

    @staticmethod
    def track(row):
        return {
            "id": row[0],
            "title": row[1],
            "url": row[2],
            "streams": row[3],
            "artist_id": row[5],
            "trend_id": row[6]
        }