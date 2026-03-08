from plant_api.models.plant import Plant


class Tree(Plant):

    def describe(self):
        return f"{self.name} is a tree"