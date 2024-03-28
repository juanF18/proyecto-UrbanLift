class Cab:
    def __init__(self, placa: str, capacidadTanque: int):
        self.placa = placa
        self.capacidadTanque = capacidadTanque

    def load_cabs(data: dict):
        cabs = []
        for cab_data in data["taxis"]:
            cab = Cab(
                cab_data["placa"],
                cab_data["capacidad_tanque"],
            )
            cabs.append(cab)
        return cabs

    def obtenerPlaca(self):
        return self.placa

    def asignarPlaca(self, unaPlaca: str):
        if unaPlaca is not None:
            self.placa = unaPlaca

    def obtenerCapacidad(self):
        return self.capacidadTanque

    def asignarCapacidad(self, unaCapacidad: int):
        if unaCapacidad is not None:
            self.capacidadTanque = unaCapacidad
