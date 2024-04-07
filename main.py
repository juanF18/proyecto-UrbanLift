from Models.Node import Node
from Models.Cab import Cab
from func.data_loading import extract_data
from Models.Routes import Routes
from func.node_paths import Node_paths
from copy import deepcopy
import random


def main():
    path_data = "./data/datos2.json"

    data = extract_data(path_data)

    # dictionary of all nodes
    nodes = Node.load_nodes(data)

    # Array of all cabs
    cabs = Cab.load_cabs(data)

    # call bfs
    routes_bfs = Routes()

    # functions of node routes
    routes = Node_paths()

    # Assign random cabs into nodes
    newCabs = deepcopy(cabs)
    nodeKeys = list(nodes.keys())
    assignCabs(newCabs, nodeKeys, nodes)

    # print nodes and cabs data
    print("Nodes data")
    for k, v in nodes.items():
        print(v.nombre)

    print("Cabs data")
    for cab in cabs:
        print(cab.placa)

    start = "Nodo1"
    end = "Nodo5"

    print("A* sobre calle y carrera")
    print("Start Node: ", start)
    print("End Node: ", end)
    path = routes.astar_shortest_route(nodes, "Nodo1", "Nodo5")
    print("Path: ", path)
    print("-" * 50)

    print("Best firs search")
    inicio = "Nodo1"
    fin = "Nodo6"
    path = routes_bfs.bestFirstSearch(nodes, inicio, fin)
    nodo = fin
    camino = [nodo]
    while nodo != (inicio):
        nodo = path[nodo]
        camino.append(nodo)

    camino.reverse()
    print("Path: ", camino)
    print("-" * 50)
    print("Route a* with lower fuel consumption")
    Node.resetting_euristics_values(nodes)
    path, total_fuel = routes.astar_with_gas(nodes, "Nodo1", "Nodo5", 15)
    print("Path: ", path)
    print("Total fuel expense was: ", total_fuel)

    # Route hill climbing

    iteraciones_max = 50
    pathHill = routes_bfs.hillClimbing(nodes, inicio, fin, iteraciones_max)
    print(pathHill)


""" 
    Method to asign random cabs into nodes
    Args:
        cabList:list
        nodeKeys:list
        nodeList:dict
"""


def assignCabs(cabList: list, nodeKeys: list, nodeList: dict):
    numberCabs = len(cabList) - 1
    numberNodes = len(nodeKeys) - 1
    indexCab = -50
    indexNode = -50
    while cabList:
        indexCab = random.randint(0, numberCabs)
        indexNode = random.randint(0, numberNodes)
        nodeKey = nodeKeys.pop(indexNode)
        cab = cabList.pop(indexCab)
        node = nodeList[nodeKey]
        node.setCab(cab)
        numberCabs -= 1
        numberNodes -= 1


if __name__ == "__main__":
    main()
