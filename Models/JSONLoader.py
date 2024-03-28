import json


class JsonLoader:
    jsonPath = "../data/datos.json"

    # function to load data from json file
    def loadJSON(self):
        with open(self.jsonPath) as file:
            data = json.load(file)
