class cinta:
    cabeza=0

    def __init__(self,entrada,blanco):
        self.entrada=entrada
        self.blanco=blanco
    
    def leer(self):
        return entrada[cabeza]

    def transicion(self,escribir,mover):
        entrada[cabeza]=escribir
        if mover=="L":
            if cabeza==0:
                entrada.insert(0,blanco)
            else:
               cabeza=cabeza-1
        elif mover == "R":
            if cabeza+1>=len(entrada):
                entrada.append(blanco)
            cabeza=cabeza+1
