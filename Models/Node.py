from Models.Cab import Cab


class Node:
    def __init__(
        self,
        nombre: str,
        carrera: str,
        calle: str,
        semaforo: dict,
        puntoInteres: bool,
        conexiones: list,
        cab: Cab,
    ):
        self.nombre = nombre
        self.carrera = carrera
        self.calle = calle
        self.semaforo = semaforo
        self.puntoInteres = puntoInteres
        self.conexiones = conexiones
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None
        self.cab = cab

    def __eq__(self, other):
        """
        Used when a compared == is called to compare 2 objects.
        """
        return self.nombre == other.nombre

    def __lt__(self, other):
        """
        compares the values of the total cost function f of two
        nodes and returns True if the value of f of the current
        node is less than the value of f of the other node, and False otherwise.
        """
        return self.f < other.f

    def __hash__(self):
        """
        Is used to obtain the hash of an object of the Node class.
        In this case, it uses the node's name attribute
        """
        return hash(self.nombre)

    def resetting_euristics_values(nodes_dict: dict):
        for k, v in nodes_dict.items():
            v.f = 0
            v.g = 0
            v.h = 0
        return True

    def load_nodes(data: dict):
        """
        Loads nodes from a data dictionary and returns a list of Node
        objects and loads the nodes associated with it into connections

        Args:
            data(dict): a dictionary containing the
            information of the nodes
        Returns:
            dict: A dict of Nodes objects created
        a list of Node object.JFC-4
            from the data provided
            .
        """
        # diccionario de nodos
        nodes = {}
        # Diccionario para mapear los nombres de la conexiones de los nodos
        node_map = {}
        for nodo_data in data["nodes"]:
            nodo = Node(
                nodo_data["nombre"],
                nodo_data["carrera"],
                nodo_data["calle"],
                nodo_data["semaforo"],
                nodo_data["punto_de_interes"],
                [],
                None,
            )
            nodes[nodo.nombre] = nodo
            # Agregamos el nombre del nodo al mapeo
            node_map[nodo.nombre] = nodo_data["conexiones"]
        # Se agregan las conexiones conexiones como objeto nodos
        for k, v in nodes.items():
            v.conexiones = [nodes[conexion] for conexion in node_map[k]]

        return nodes

    # Method to set new value to node name
    def set_nombre(self, nuevoNombre: str):
        self.nombre = nuevoNombre

    # Method to get attribute name of node
    def get_nombre(self) -> str:
        return self.nombre

    # Method to set attribute carrera of node
    def set_carrera(self, nuevaCarrera: str):
        self.carrera = nuevaCarrera

    # Method to get attribute carrera of node
    def get_carrera(self):
        return self.carrera

    # Method to set attribute calle of node
    def set_calle(self, nuevaCalle: str):
        self.calle = nuevaCalle

    # Method to get attribute calle of node
    def get_calle(self):
        return self.calle

    # Method to set attribute semaforo of node
    def set_semaforo(self, nuevoEstado: bool):
        self.semaforo = nuevoEstado

    # Method to get of attribute semaforo
    def get_semaforo(self):
        return self.semaforo

    # Method to set new state of punto interes attribute
    def set_punto_interes(self, nuevoEstado: bool):
        if nuevoEstado is not None:
            self.puntoInteres = nuevoEstado

    # Method to get cab into node
    def getCab(self):
        return self.cab

    # Method to set cab into node
    def setCab(self, aCab: Cab):
        if aCab != None:
            self.cab = aCab
