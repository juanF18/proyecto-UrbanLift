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
        )  # El costo inicial es 0

        while open_list:
            _, current_node = heapq.heappop(open_list)
            closed_list.add(current_node.nombre)

            if current_node == end_node:
                path = []
                total_fuel_consumption = (
                    current_node.g
                )  # El consumo total de combustible
                while current_node:
                    path.append(current_node.nombre)
                    current_node = current_node.parent
                return (
                    path[::-1],
                    total_fuel_consumption,
                )  # Devuelve también el consumo total de combustible

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
