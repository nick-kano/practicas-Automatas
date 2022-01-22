import json 

class js:
    def __init__(self):
        self.x = open("M.json")
        self.m = json.loads(x)
        self.x.close()
        self.estados = m["Estados"]
        self.entrada = m["Entrada"]
        self.cinta = m["Cinta"]
        self.inicial = m["Inicial"]
        self.blanco = m["Blanco"]
        self.finales = m["Finales"]
        self.transiciones = m["Transiciones"]
