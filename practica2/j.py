import json 

class j:
    def _init_():
        x = open("M.json")
        m = json.loads(x)
        x.close()
        estados = m["Estados"]
        entrada = m["Entrada"]
        cinta = m["Cinta"]
        inicial = m["Inicial"]
        blanco = m["Blanco"]
        finales = m["Finales"]
        transiciones = m["Transiciones"]
