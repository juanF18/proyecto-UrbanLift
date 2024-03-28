from Models.Node import Node
from func.data_loading import extract_data


def main():
    path_data = "./data/datos.json"

    data = extract_data(path_data)

    # Array of all nodes
    nodes = Node.load_nodes(data)

    for node in nodes:
        print(node.nombre)


if __name__ == "__main__":
    main()
