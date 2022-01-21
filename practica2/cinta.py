class cinta:
    cabeza=0

    def __init__(self,entrada):
        self.entrada=entrada
    
    def leer(self):
        return entrada[cabeza]

    def transicion(self,escribir,mover):
        entrada[cabeza]=escribir
        if mover=="L":
            if cabeza==0:
                entrada.insert(0,"_")
            else:
               cabeza=cabeza-1
        elif mover == "R":
            if cabeza+1>=len(entrada):
                entrada.append("_")
            cabeza=cabeza+1