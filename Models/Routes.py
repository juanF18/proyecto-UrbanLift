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
