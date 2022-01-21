class trancision:
        simbolo = None
        estado = None
        direccion = None

    def __init__(self,trancisiones):
        self.trancisiones = trancisiones

    def existe(self,estado,simbolo):
        for x in trancisiones:
            if x[0] == estado and x[1] == simbolo:
                estado = x[2]
                simbolo = x[3]
                direccion = x[4]
                return True
        return False

    def simbolo(self):
        return simbolo

    def direccion(self):
        return direccion

    def estado(self):
        return estado