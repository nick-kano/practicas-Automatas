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
        return estadoActual in finales

    def mover(self):
        simbolo=cinta.leer()
        if transicion.existe(estadoActual,simbolo):
            cinta.transicion(transicion.simbolo(),transicion.direccion())
            estadoActual=transicion.siguienteEstado()
            return 0
        else:
            if acepta():
                return 1
            else:
                return -1