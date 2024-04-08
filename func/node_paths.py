from collections import deque
import heapq


class Node_paths:
    def __init__(self) -> None:
        pass

    """
    Calculates the heuristic estimate of the cost to reach the end node from the given node. 
    This heuristic is used in pathfinding algorithms to estimate distances between nodes on a grid.

    Parameters:

        node: The current node from which the heuristic cost to the end node is being calculated.
        end: The end node for which the heuristic cost is being calculated from the current node.

    Returns:

        int: The estimated cost from the current node to the end node.
    """

    def __calculate_heuristic(self, node, end):
        return abs(node.calle - end.calle) + abs(node.carrera - end.carrera)

    """
    Calculates the cost of traveling from a node to its neighbor, considering the efficiency of 
    the vehicle being used.
    Parameters:

        node: The current node from which the neighbor's cost is being calculated.
        neighbor: The neighboring node to which the cost is calculated.
        vehicle_efficiency: A measure of the vehicle's efficiency, used to calculate the cost.

    Returns:

        float: The calculated cost to travel from node to neighbor.
    """

    def __calculate_cost(self, node, neighbor, vehicle_efficiency):
        distance = abs(node.calle - neighbor.calle) + abs(
            node.carrera - neighbor.carrera
        )

        return distance / vehicle_efficiency

    """
        Finds the shortest route between two nodes using the A* search algorithm.
    Parameters:

        nodes_dict: A dictionary of node objects accessible by their names.
        start_name: The name of the start node.
        end_name: The name of the end node.

    Returns:

        list: A list of node names representing the shortest path from the start node
        to the end node. If no path exists, returns None.
    """

    def astar_shortest_route(self, nodes_dict, start_name, end_name):
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

    """
    Finds the shortest route between two nodes using the A* search algorithm, considering 
    the vehicle's fuel efficiency.
    Parameters:

        nodes_dict: A dictionary of node objects accessible by their names.
        start_name: The name of the start node.
        end_name: The name of the end node.
        vehicle_efficiency: The efficiency of the vehicle being used, which affects the 
        cost of travel between nodes.

    Returns:

        tuple: A tuple containing a list of node names representing the shortest path from 
        the start node to the end node and the total fuel consumption for this path. If no path exists, returns None.
    """

    def astar_with_gas(self, nodes_dict, start_name, end_name, vehicle_efficiency):
        open_list = []
        closed_list = set()

        start_node = nodes_dict[start_name]
        end_node = nodes_dict[end_name]

        heapq.heappush(
            open_list, (start_node.nombre, start_node)
        )  # The initial cost is 0

        while open_list:
            _, current_node = heapq.heappop(open_list)
            closed_list.add(current_node.nombre)

            if current_node == end_node:
                path = []
                total_fuel_consumption = current_node.g  # Total fuel consumption
                while current_node:
                    path.append(current_node.nombre)
                    current_node = current_node.parent
                return (
                    path[::-1],
                    total_fuel_consumption,
                )  # Returns also the total fuel consumption

            for neighbor in current_node.conexiones:
                if neighbor.nombre in closed_list:
                    continue

                tentative_g = current_node.g + self.__calculate_cost(
                    current_node, neighbor, vehicle_efficiency
                )
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

    """
    This function performs a breadth-first search (BFS) to find the shortest path 
    between a start node and a target node in a graph. It returns the sequence of nodes that form this path.
    Parameters:

        start_node (str): The starting node for the BFS.
        target_node (str): The node to find the path to, from the start_node.

    Returns:

        list of Node: A list of nodes representing the shortest path from start_node 
        to target_node. Returns None if no path exists.
    """

    def bfs_find_path(self, start_node, target_node):
        visited = set()
        queue = deque()
        queue.append((start_node, [start_node]))

        while queue:
            current_node, path = queue.popleft()
            if current_node == target_node:
                return path

            for connection in current_node.conexiones:
                if connection not in visited:
                    visited.add(connection)
                    new_path = list(path)
                    new_path.append(connection)
                    queue.append((connection, new_path))

        return None

    """
    This function designs a tour, starting from a given node, that aims to visit all
    points of interest in a graph using a modified best-first search strategy. It 
    returns the names of the nodes in the order they are visited.
    Parameters:

        start_node_name (str): The name of the starting node for the tour.
        nodos (dict): A dictionary of nodes accessible by their names. Each node is 
        expected to have attributes like nombre (name), puntoInteres (whether it's a 
        point of interest), and connections to other nodes.

    Returns:

        list of str: A list of node names representing the tour path that visits all 
        points of interest and returns to the start node, if possible.
    """

    def path_tour_trip_best_first_search(self, start_node_name, nodos):
        start_node = nodos[start_node_name]
        points_of_interest = [
            node for node in nodos.values() if node.puntoInteres and node != start_node
        ]
        path = [start_node]
        current_node = start_node

        while points_of_interest:
            closest_path = None
            for point in points_of_interest:
                temp_path = self.bfs_find_path(current_node, point)
                if temp_path and (
                    closest_path is None or len(temp_path) < len(closest_path)
                ):
                    closest_path = temp_path

            if closest_path:
                # Avoid adding the current node twice if it's already at the end of the path
                if path[-1] == closest_path[0]:
                    path.extend(closest_path[1:])
                else:
                    path.extend(closest_path)
                current_node = closest_path[-1]
                points_of_interest.remove(current_node)
            else:
                break  # If no path is found to any of the remaining points, break out of the loop

        if path[-1] != start_node:
            return_path_to_start = self.bfs_find_path(current_node, start_node)
            if return_path_to_start:
                # Make sure not to duplicate the current node in the path.
                if return_path_to_start[0] == path[-1]:
                    path.extend(return_path_to_start[1:])
                else:
                    path.extend(return_path_to_start)

        return [node.nombre for node in path]
