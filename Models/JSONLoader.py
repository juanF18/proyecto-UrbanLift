import json
from .Taxi import Taxi


class JsonLoader:
    jsonPath = "./data/datos.json"
    __taxis = []
    __nodes = []

    # Method to get a copy of added nodes
    def getNodes(self):
        return self.__nodes.copy

    # Method to get a copy of added taxis
    def getTaxis(self):
        return self.__taxis.copy

    # function to load data from json file
    def loadJSON(self):
        with open(self.jsonPath) as file:
            data = json.load(file)

        self.createVehicles(data["taxis"])
        self.createNodes(data["nodos"])

    # function for create list of vehicles, vehicles are received as argument
    def createVehicles(self, vehicles: dict):
        for vehicle in vehicles:
            taxi = Taxi(vehicle["placa"], vehicle["capacidad_tanque"])
            self.__taxis.append(taxi)

    # function for create list of nodes, nodes area received as argument
    def createNodes(self, nodes: dict):
        for node in nodes:
            print()
            # node = Node(
            #     node["nombre"],
            #     node["carrera"],
            #     node["calle"],
            #     node["semaforo"],
            #     node["punto_de_interes"],
            #     node["conexiones"],
            # )
            # self.__nodes.append(node)
