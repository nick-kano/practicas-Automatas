import json 

class JsonUwU:
    def __init__(self,cadena):
        self.x = open(cadena)
        self.m = json.loads(x)
        self.estados = m["Estados"]
        self.entrada = m["Entrada"]
        self.cinta = m["Cinta"]
        self.inicial = m["Inicial"]
        self.blanco = m["Blanco"]
        self.finales = m["Finales"]
        self.transiciones = m["Transiciones"]
