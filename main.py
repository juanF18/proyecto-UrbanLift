from Models.Node import Node
from Models.Cab import Cab
from func.data_loading import extract_data
from Models.Routes import Routes
from func.node_paths import Node_paths
from copy import deepcopy
import math
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
    matrix = generate_matrix(list(nodes.keys()))
    print("-" * 25, "MAPA DE LA CIUDAD", "-" * 25)
    print_matrix(matrix)
    print("-" * 60)
    origen = seleccionar_nodo(list(nodes.keys()), "Seleccione el Nodo de Origen:")
    destino = seleccionar_nodo(list(nodes.keys()), "Seleccione el Nodo de Destino:")
    print("Selected route from user to taxi")
    path_taxi = routes_bfs.astarShortestRoute(nodes, origen)[::-1]
    print(path_taxi)
    cab = nodes[path_taxi[0]].getCab().get_plate()
    print("Placa taxi: ", cab)
    print(f"El origin escogido fue {origen} y el destino fue {destino}")
    print(
        """
    Seleccione el tipo de ruta deseada:
    [1] Ruta más corta
    [2] Ruta más rápida
    [3] Ruta con menor consumo de combustible
    [4] Ruta más económica para el pasajero
    [5] Tour Trip
    """
    )
    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        print("La ruta mas corta fue: ")
        path_short = routes.astar_shortest_route(nodes, origen, destino)
        total_distance, fuel_consumption, total_time, total_cost = (
            Cab.generate_travel_report(path_short, nodes)
        )
        print("Paso a Paso")
        print_path(path_short, matrix)
        print("Path: ", path_short)
        print(
            f"Total distance: {total_distance} km\n Fuel consuption: {fuel_consumption} km/l \n Total time: {total_time} min\n Total cost: {total_cost} $"
        )
        Node.resetting_euristics_values(nodes)
    elif opcion == 2:
        print("La ruta mas rapida fue: ")
        path_fast = routes_bfs.bestFirstSearch(nodes, origen, destino)
        camino = execute_fastest_path(origen, destino, path_fast)
        total_distance, fuel_consumption, total_time, total_cost = (
            Cab.generate_travel_report(camino, nodes)
        )
        print("Paso a Paso")
        print_path(camino, matrix)
        print("Path: ", camino)
        print(
            f"Total distance: {total_distance} km\n Fuel consuption: {fuel_consumption} km/l \n Total time: {total_time} min\n Total cost: {total_cost} $"
        )
    elif opcion == 3:
        print("La ruta con menos consumo de gas fue: ")
        path_with_gas, _ = routes.astar_with_gas(nodes, origen, destino, 1)
        print("Paso a Paso")
        print_path(path_with_gas, matrix)
        print("Path: ", path_with_gas)
        total_distance, fuel_consumption, total_time, total_cost = (
            Cab.generate_travel_report(path_with_gas, nodes)
        )
        print(
            f"Total distance: {total_distance} km\n Fuel consuption: {fuel_consumption} km/l \n Total time: {total_time} min\n Total cost: {total_cost} $"
        )
        Node.resetting_euristics_values(nodes)
        print("-" * 25, " Comparativa con las otra rutas ", "-" * 25)
        report_of_all_routes(origen, destino, nodes, routes, routes_bfs)
    elif opcion == 4:
        print("La ruta mas economica fue: ")
        iteraciones_max = 50
        path_hill = routes_bfs.hillClimbing(nodes, origen, destino, iteraciones_max)
        print("Paso a Paso")
        print_path(path_hill, matrix)
        print("Path: ", path_hill)
        total_distance, fuel_consumption, total_time, total_cost = (
            Cab.generate_travel_report(path_hill, nodes)
        )
        print(
            f"Total distance: {total_distance} km\n Fuel consuption: {fuel_consumption} km/l \n Total time: {total_time} min\n Total cost: {total_cost} $"
        )
    elif opcion == 5:
        print("La ruta que tomo para el Tour Trip fue:")
        path_tour_trip = routes.path_tour_trip_best_first_search(origen, nodes)
        print("Paso a Paso")
        print_path(path_tour_trip, matrix)
        print(path_tour_trip)
        total_distance, fuel_consumption, total_time, total_cost = (
            Cab.generate_travel_report(path_tour_trip, nodes)
        )
        print(
            f"Total distance: {total_distance} km\n Fuel consuption: {fuel_consumption} km/l \n Total time: {total_time} min\n Total cost: {total_cost} $"
        )
    else:
        print("Opción no válida.")


def print_matrix(matriz):
    # Determinar la longitud máxima de los elementos de la matriz
    # para ajustar el tamaño de los cuadrados/rectángulos
    max_len = max(len(str(item)) for row in matriz for item in row)

    # Definir el borde superior e inferior de cada celda
    borde_horizontal = "+" + ("-" * (max_len + 2))
    borde_horizontal = borde_horizontal * len(matriz[0]) + "+"

    for fila in matriz:
        # Imprimir el borde superior de la fila
        print(borde_horizontal)
        # Imprimir el contenido de la fila
        fila_str = "| " + " | ".join(str(item).center(max_len) for item in fila) + " |"
        print(fila_str)
    # Imprimir el borde inferior de la última fila
    print(borde_horizontal)


def generate_matrix(list_nodes):
    n = math.ceil(math.sqrt(len(list_nodes)))

    matriz = []

    for i in range(n):
        fila = []
        for j in range(n):
            # Calcular el índice del nodo en la lista plana
            index = i * n + j
            if index < len(list_nodes):
                fila.append(list_nodes[index])
            else:
                fila.append(None)
        matriz.append(fila)

    return matriz


def print_path(path, matrix):
    new_matrix = deepcopy(matrix)
    path_set = set(path)

    for x in range(len(new_matrix)):
        for y in range(len(new_matrix[x])):
            if new_matrix[x][y] in path_set:
                new_matrix[x][y] += "*"
                print("-" * 25)
                print_matrix(new_matrix)
                print("-" * 25)


def report_of_all_routes(start, end, nodes, routes, routes_bfs):
    # ------------------ Shortes path -------------------------
    print("Reporte ruta mas corta: ")
    path_short = routes.astar_shortest_route(nodes, start, end)
    total_distance, fuel_consumption, total_time, total_cost = (
        Cab.generate_travel_report(path_short, nodes)
    )
    print("Path: ", path_short)
    print(
        f"Total distance: {total_distance} km\n Fuel consuption: {fuel_consumption} km/l \n Total time: {total_time} min\n Total cost: {total_cost} $"
    )
    Node.resetting_euristics_values(nodes)
    # ------------------ Fastest path -------------------------
    print("Reporte ruta mas rapida: ")
    path_fast = routes_bfs.bestFirstSearch(nodes, start, end)
    camino = execute_fastest_path(start, end, path_fast)
    total_distance, fuel_consumption, total_time, total_cost = (
        Cab.generate_travel_report(camino, nodes)
    )
    print("Path: ", camino)
    print(
        f"Total distance: {total_distance} km\n Fuel consuption: {fuel_consumption} km/l \n Total time: {total_time} min\n Total cost: {total_cost} $"
    )
    # ------------------ Cheapest path ------------------------
    print("Reporte ruta mas economica: ")
    iteraciones_max = 50
    pathHill = routes_bfs.hillClimbing(nodes, start, end, iteraciones_max)
    print("Path: ", pathHill)
    total_distance, fuel_consumption, total_time, total_cost = (
        Cab.generate_travel_report(pathHill, nodes)
    )
    print(
        f"Total distance: {total_distance} km\n Fuel consuption: {fuel_consumption} km/l \n Total time: {total_time} min\n Total cost: {total_cost} $"
    )


def execute_fastest_path(origen, destino, path):
    nodo = destino
    camino = [nodo]
    while nodo != (origen):
        nodo = path[nodo]
        camino.append(nodo)
    camino.reverse()
    return camino


def seleccionar_nodo(nodos, mensaje):
    print(mensaje)
    for i, nodo in enumerate(nodos, start=1):
        print(f"[{i}] {nodo}")

    seleccion_valida = False
    seleccion = -1
    while not seleccion_valida:
        try:
            seleccion = int(input("Seleccione el número del nodo: ")) - 1
            if 0 <= seleccion < len(nodos):
                seleccion_valida = True
            else:
                print("Por favor, seleccione un número válido de la lista.")
        except ValueError:
            print("Por favor, ingrese un número.")

    return nodos[seleccion]


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
