from queue import PriorityQueue
import heapq


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

    def astarShortestRoute(self, nodes_dict, start_name, end_name):
        open_list = []
        closed_list = set()

        start_node = nodes_dict[start_name]
        end_node = nodes_dict[end_name]

        heapq.heappush(open_list, (start_node.nombre, start_node))

        while open_list:
            _, current_node = heapq.heappop(open_list)
            closed_list.add(current_node.nombre)

            if current_node == end_node:
                path = []
                while current_node:
                    path.append(current_node.nombre)
                    current_node = current_node.parent
                return path[::-1]

            for neighbor in current_node.conexiones:
                if neighbor.nombre in closed_list:
                    continue

                tentative_g = current_node.g + 1
                tentative_f = tentative_g + self.__calculate_heuristic(
                    neighbor, end_node
                )

                in_open_list = False
                for item in open_list:
                    _, open_node = item
                    if neighbor.nombre == open_node.nombre:
                        in_open_list = True
                        if tentative_g >= neighbor.g:
                            break
                if not in_open_list or tentative_g < neighbor.g:
                    neighbor.g = tentative_g
                    neighbor.h = self.__calculate_heuristic(neighbor, end_node)
                    neighbor.f = tentative_f
                    neighbor.parent = current_node
                    if not in_open_list:
                        heapq.heappush(open_list, (neighbor.nombre, neighbor))

        return None
