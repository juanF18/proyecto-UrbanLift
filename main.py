from Models.Node import Node
from Models.Cab import Cab
from func.data_loading import extract_data
from Models.Routes import Routes
from func.node_paths import Node_paths


def main():
    path_data = "./data/datos2.json"

    data = extract_data(path_data)

    # dictionary of all nodes
    nodes = Node.load_nodes(data)

    # Array of all cabs
    cabs = Cab.load_cabs(data)

    routes = Routes()
    routes.bestFirstSearch(nodes, "Nodo1", "Nodo8")
    # functions of node routes
    routes = Node_paths()

    print("Nodes data")
    for k, v in nodes:
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


if __name__ == "__main__":
    main()
