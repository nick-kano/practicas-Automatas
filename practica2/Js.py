import json 

class JsonUwU:

    def __init__(self,maquina):
        m = json.load(maquina)
        self.estados = m["Estados"]
        self.entrada = m["Entrada"]
        self.cinta = m["Cinta"]
        self.inicial = m["Inicial"]
        self.blanco = m["Blanco"]
        self.finales = m["Finales"]
        self.transiciones = m["Transiciones"]
