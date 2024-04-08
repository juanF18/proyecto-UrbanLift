class Cab:
    def __init__(self, placa: str, capacidadTanque: int):
        self.placa = placa
        self.capacidadTanque = capacidadTanque

    def generate_travel_report(route, nodes):
        # Constants
        distance_per_node = 10  # km
        fuel_efficiency = 15  # km/litre
        base_time_per_node = 10  # minutes
        cost_per_km = 3000  # Colombian pesos

        # Calculating total distance traveled
        total_distance = (len(route) - 1) * distance_per_node

        # Calculating fuel consumption
        fuel_consumption = total_distance / fuel_efficiency

        # Calculating total cost of the trip
        total_cost = total_distance * cost_per_km

        # Calculating total time
        total_time = (
            len(route) - 1
        ) * base_time_per_node  # Base time without considering traffic lights
        # Adding extra time for traffic lights
        for node in route[:-1]:
            # The last node is not considered for travel time
            if nodes[node].semaforo["have"]:
                total_time += (
                    nodes[node].semaforo["duration"] * 60
                )  # Convert hours to minutes

        return total_distance, fuel_consumption, total_time, total_cost

    def load_cabs(data: dict):
        cabs = []
        for cab_data in data["taxis"]:
            cab = Cab(
                cab_data["placa"],
                cab_data["capacidad_tanque"],
            )
            cabs.append(cab)
        return cabs

    def get_plate(self):
        return self.placa

    def set_plate(self, unaPlaca: str):
        if unaPlaca is not None:
            self.placa = unaPlaca

    def get_capacity(self):
        return self.capacidadTanque

    def set_capacity(self, unaCapacidad: int):
        if unaCapacidad is not None:
            self.capacidadTanque = unaCapacidad
