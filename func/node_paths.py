from collections import deque
import heapq


class Node_paths:
    def __init__(self) -> None:
        pass

    def __calculate_heuristic(self, node, end):
        return abs(node.calle - end.calle) + abs(node.carrera - end.carrera)

    def __calculate_cost(self, node, neighbor, vehicle_efficiency):
        distance = abs(node.calle - neighbor.calle) + abs(
            node.carrera - neighbor.carrera
        )

        return distance / vehicle_efficiency

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
