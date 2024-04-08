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

    # call bfs
    routes_bfs = Routes()

    # functions of node routes
    routes = Node_paths()

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
    print("-" * 50)
    print("Route with Hill climb")
    iteraciones_max = 50
    pathHill = routes_bfs.hillClimbing(nodes, inicio, fin, iteraciones_max)
    print("Path: ", pathHill)
    print("-" * 50)
    print("Tour trip")
    path_tour_trip = routes.path_tour_trip_best_first_search("Nodo3", nodes)
    print(path_tour_trip)


if __name__ == "__main__":
    main()
