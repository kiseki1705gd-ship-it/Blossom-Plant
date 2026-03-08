class Plant:

    def __init__(self, id, name, scientific_name):
        self._id = id
        self._name = name
        self._scientific_name = scientific_name

    def describe(self):
        return "This is a plant"

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "scientific_name": self._scientific_name
        }