from plant_api.models.flower import Flower
from plant_api.models.tree import Tree


class PlantService:

    def __init__(self, repository):
        self.repository = repository

    def get_all_plants(self):
        plants = self.repository.get_all()
        return [p.to_dict() for p in plants]

    def add_plant(self, data):

        if data["type"] == "flower":
            plant = Flower(
                data["id"],
                data["name"],
                data["scientific_name"],
                data.get("biome", "Unknown"),
                data.get("created_at")
            )

        elif data["type"] == "tree":
            plant = Tree(
                data["id"],
                data["name"],
                data["scientific_name"],
                data.get("biome", "Unknown"),
                data.get("created_at")
            )

        else:
            raise ValueError("Unknown plant type")

        self.repository.add(plant)

        return plant.to_dict()