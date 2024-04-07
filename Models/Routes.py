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

    def hillClimbing(self, L, inicio, final, iteraciones_max=100):
        pos_actual = inicio
        valor_actual = self.heuristicHill(L, pos_actual, final)

        for _ in range(iteraciones_max):
            candidatos = [
                (pos_actual[0] + 1, pos_actual[1]),
                (pos_actual[0] - 1, pos_actual[1]),
                (pos_actual[0], pos_actual[1] + 1),
                (pos_actual[0], pos_actual[1] - 1),
            ]

            candidatos = []

            if not candidatos:
                break

            candidato = max(candidatos, key=lambda n: self.heuristicHill(L, n, final))
            valor_candidato = self.heuristicHill(L, candidato, final)

            if valor_candidato > valor_actual:
                L[pos_actual[0]][pos_actual[1]] = 2
                pos_actual = candidato
                valor_actual = valor_candidato

            if pos_actual == final:
                L[pos_actual[0]][pos_actual[1]] = 2
                print("¡Objetivo alcanzado!")
                break

        return L

    def heuristicHill(self, L, pos_actual, final):
        return -(
            ((pos_actual[0] - final[0]) ** 2 + (pos_actual[1] - final[1]) ** 2) ** 0.5
        )
