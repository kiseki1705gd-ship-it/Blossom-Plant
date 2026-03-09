from datetime import datetime


class Plant:

    def __init__(self, id, name, scientific_name, biome, created_at=None):
        self._id = id
        self._name = name
        self._scientific_name = scientific_name
        self._biome = biome
        self._created_at = created_at or datetime.now().isoformat()

    def describe(self):
        return "This is a plant"

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "scientific_name": self._scientific_name,
            "biome": self._biome,
            "created_at": self._created_at
        }