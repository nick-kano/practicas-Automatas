class MaquinaTuring:
    
    def __init__(self,estados,entrada,cinta,inicial,blanco,finales,transicion):
        self.estados = estados          #Lista de string
        self.entrada = entrada          #lista de string
        self.cinta = cinta              #objeto cinta
        self.inicial = inicial          #string
        self.blanco = blanco            #char
        self.finales = finales          #lista de string
        self.transicion = transicion    #objeto transicion
        self.estadoActual=inicial       #string

    def acepta(self):
        return self.estadoActual in self.finales

    def mover(self):
        simbolo=self.cinta.leer()
        if self.transicion.existe(self.estadoActual,simbolo):
            self.cinta.transicion(self.transicion.estado,self.transicion.simbolo,self.transicion.direccion)
            self.estadoActual=self.transicion.estado
            return 0
        else:
            if self.acepta():
                return 1
            else:
                return -1
