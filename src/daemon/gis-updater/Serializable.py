class Serializable:

    @staticmethod
    def region(obj):
        return {
            "name": obj[0],
            "lat": obj[1],
            "lon": obj[2]
        }