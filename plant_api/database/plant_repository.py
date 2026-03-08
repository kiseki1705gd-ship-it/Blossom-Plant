from abc import ABC, abstractmethod


class PlantRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def add(self, plant):
        pass