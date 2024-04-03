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
            nodeList: list
            start:touple
            finish:touple
    """

    def bestFirstSearch(self, nodeL, start, finish):
        queue = PriorityQueue()
        queue.put((0, start))
        predecessors = {}
        predecessors[start] = None
        while queue:
            _, node = queue.get()
            if node == finish:
                break
            for m in self.__MOVEMENTS:
                f = node[0] + m[0]
                c = node[1] + m[1]
                if 0 <= f < len(nodeL) and 0 <= c < len(nodeL[0]) and nodeL[f][c] == 0:
                    newNode = (f, c)
                    if newNode not in predecessors:
                        prioridad = self.heuristicBFS(newNode, finish)
                        queue.put((prioridad, newNode))
                        predecessors[newNode] = node
        return predecessors

    """ 
        method to calculate a heuristic for two nodes for BFS algorithm
        args:
            nodeA:touple
            nodeB:touple
    """

    def heuristicBFS(nodeA, nodeB):
        return abs(nodeA[0] - nodeB[0]) + abs(nodeA[1] - nodeB[1])
