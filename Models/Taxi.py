class Taxi:
    def __init__(self, placa: str, capacidadTanque: int):
        self.placa = placa
        self.capacidadTanque=capacidadTanque

    def obtenerPlaca(self):
        return self.placa

    def asignarPlaca(self, unaPlaca:str):
        if unaPlaca != None:
            self.placa=unaPlaca            

    def obtenerCapacidad(self):
        return self.capacidadTanque
    
    def asignarCapacidad(self, unaCapacidad: int):
        if unaCapacidad !=None:
            self.capacidadTanque=unaCapacidad           
            

    
        
    
        
    
        

    
