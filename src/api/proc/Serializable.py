class Serializable:

    @staticmethod
    def find_by_region(row):
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