class MaquinaTuring:

    def __init__(self,estados,entrada,cinta,inicial,blanco,finales,transicion):
        self.estados = estados
        self.entrada = entrada
        self.cinta = cinta
        self.inicial = inicial
        self.blanco = blanco
        self.finales = finales
        self.transicion = transicion
        self.estadoActual=inicial

    def acepta(self):
        return estadoActual in finales

    def mover(self):
        simbolo=cinta.leer()
        siguiente=transicion.siguiente(estadoActual,simbolo)
        cinta.transicion(simbolo,siguiente[0],siguiente[1])
        estadoActual=siguiente[2]