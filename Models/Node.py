class Node:
    def __init__(
        self,
        nombre: str,
        carrera: str,
        calle: str,
        semaforo: bool,
        puntoInteres: bool,
        conexiones: list,
    ):
        self.nombre = nombre
        self.carrera = carrera
        self.calle = calle
        self.semaforo = semaforo
        self.puntoInteres = puntoInteres
        self.conexiones = conexiones

    def load_nodes(data: dict):
        """
        Loads nodes from a data dictionary and returns
        a list of Node object.

        Args:
            data(dict): a dictionary containing the
            information of the nodes
        Returns:
            list: A list of Node objects created
            from the data provided.
        """
        nodes = []
        for nodo_data in data["nodes"]:
            nodo = Node(
                nodo_data["nombre"],
                nodo_data["carrera"],
                nodo_data["calle"],
                nodo_data["semaforo"],
                nodo_data["punto_de_interes"],
                nodo_data["conexiones"],
            )
            nodes.append(nodo)
        return nodes

    # Method to set new value to node name
    def setNombre(self, nuevoNombre: str):
        self.nombre = nuevoNombre

    # Method to get attribute name of node
    def getNombre(self) -> str:
        return self.nombre

    # Method to set attribute carrera of node
    def setCarrera(self, nuevaCarrera: str):
        self.carrera = nuevaCarrera

    # Method to get attribute carrera of node
    def getCarrera(self):
        return self.carrera

    # Method to set attribute calle of node
    def setCalle(self, nuevaCalle: str):
        self.calle = nuevaCalle

    # Method to get attribute calle of node
    def getCalle(self):
        return self.calle

    # Method to set attribute semaforo of node
    def setSemaforo(self, nuevoEstado: bool):
        self.semaforo = nuevoEstado

    # Method to get of attribute semaforo
    def get_semaforo(self):
        return self.semaforo

    # Method to set new state of punto interes attribute
    def setPuntoInteres(self, nuevoEstado: bool):
        if nuevoEstado is not None:
            self.puntoInteres = nuevoEstado
