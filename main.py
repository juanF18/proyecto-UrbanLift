from Models.Node import Node
from Models.Cab import Cab
from func.data_loading import extract_data


def main():
    path_data = "./data/datos.json"

    data = extract_data(path_data)

    # Array of all nodes
    nodes = Node.load_nodes(data)

    # Array of all cabs
    cabs = Cab.load_cabs(data)

    print("Nodes data")
    for node in nodes:
        print(node.nombre)

    print("Cabs data")
    for cab in cabs:
        print(cab.placa)


if __name__ == "__main__":
    main()
