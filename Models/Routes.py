from queue import PriorityQueue


class Routes:
    __TWITHTRAFFICTLIGHT = 12
    __TWITHOUTRAFFICLIGHT = 10
    __DISTANCE = 2
    __FUELCONSUPTION = 1
    __COSTNODE = 3000
    __MOVEMENTS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    """ 
        method to browse on node list and get back route from origin
        to destination
        Args:
            nodeList: dict
            start:str
            finish:str
    """

    def bestFirstSearch(self, nodeL, start, finish):
        queue = PriorityQueue()
        nodeStart = nodeL[start]
        nodeFinish = nodeL[finish]
        queue.put((0, nodeStart))
        predecessors = {}
        predecessors[nodeStart.get_nombre()] = None
        while queue:
            _, node = queue.get()
            if str.upper(node.get_nombre()) == str.upper(nodeFinish.get_nombre()):
                break
            for conectNode in node.conexiones:
                if conectNode.get_nombre() not in predecessors:
                    prioridad = self.heuristicBFS(conectNode, nodeFinish)
                    queue.put((prioridad, conectNode))
                    predecessors[conectNode.get_nombre()] = node.get_nombre()
        return predecessors

    """ 
        method to calculate a heuristic for two nodes for BFS algorithm
        args:
            newNode:node object
            finishNode:node object
    """

    def heuristicBFS(self, newNode, finishNode):
        manhattan = abs(newNode.calle - finishNode.calle) + abs(
            newNode.carrera - finishNode.carrera
        )
        if newNode.get_semaforo()["have"] == True:
            manhattan += newNode.get_semaforo()["duration"]

        return manhattan

    """ 
        method to calculate shortest route (less traffic lights)
        Args:
            nodeList: Dict
            start: str
            finish: str
    """

    def hillClimbing(self, nodeList, start: str, finish: str, iteraciones_max=100):
        startNode = nodeList[start]
        finishNode = nodeList[finish]
        posActual = startNode
        valorActual = self.heuristicHill(posActual, finishNode)
        path = [posActual.get_nombre()]
        for _ in range(iteraciones_max):
            candidatos = [node for node in posActual.conexiones]

            if not candidatos:
                break

            candidato = min(
                candidatos, key=lambda node: self.heuristicHill(node, finishNode)
            )
            valor_candidato = self.heuristicHill(candidato, finishNode)

            if valor_candidato < valorActual:
                posActual = candidato
                valorActual = valor_candidato
                path.append(posActual.get_nombre())

            if posActual.get_nombre() == finishNode.get_nombre():
                print("¡Objetivo alcanzado!")
                break

        return path

    def heuristicHill(self, actualNode, finishNode):
        manhattan = abs(actualNode.calle - finishNode.calle) + abs(
            actualNode.carrera - finishNode.carrera
        )
        if actualNode.get_semaforo()["have"] == True:
            manhattan += actualNode.get_semaforo()["duration"]

        return manhattan
