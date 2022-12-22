class Serializable:

    @staticmethod
    def artist(artist):
        return {
            "id": artist[0],
            "name": artist[1]
        }
