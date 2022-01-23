class trancision:
    simbolo = None
    estado = None
    direccion = None

    def __init__(self,trancisiones):
        self.trancisiones = trancisiones

    def existe(self,estado,simbolo):
        for x in self.trancisiones:
            if x[0] == estado and x[1] == simbolo:
                self.estado = x[2]
                self.simbolo = x[3]
                self.direccion = x[4]
                return True
        return False
