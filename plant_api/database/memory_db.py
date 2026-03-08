from plant_api.database.plant_repository import PlantRepository


class MemoryDB(PlantRepository):

    def __init__(self):
        self.plants = []

    def get_all(self):
        return self.plants

    def add(self, plant):
        self.plants.append(plant)