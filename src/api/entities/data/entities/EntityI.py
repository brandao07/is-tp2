from abc import abstractmethod, ABC


class EntityI(ABC):
    @staticmethod
    @abstractmethod
    def get_all():
        pass

    @staticmethod
    @abstractmethod
    def insert(obj):
        pass

    @staticmethod
    @abstractmethod
    def get_one(args):
        pass
