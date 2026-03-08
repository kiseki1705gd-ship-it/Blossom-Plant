from plant_api.models.plant import Plant


class Flower(Plant):

    def describe(self):
        return f"{self._name} is a flowering plant"