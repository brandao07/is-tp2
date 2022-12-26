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
    def delete(id):
        pass

    @staticmethod
    @abstractmethod
    def update(obj):
        pass

    @staticmethod
    @abstractmethod
    def get_by_id(id):
        pass
