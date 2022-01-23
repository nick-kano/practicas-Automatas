class cinta:
    cabeza=0

    def __init__(self,entrada,blanco):
        self.entrada=entrada
        self.blanco=blanco
    
    def leer(self):
        return self.entrada[self.cabeza]

    def transicion(self,escribir,mover):
        self.entrada[self.cabeza]=escribir
        if mover=="L":
            if self.cabeza==0:
                self.entrada.insert(0,self.blanco)
            else:
               self.cabeza=self.cabeza-1
        elif mover == "R":
            if self.cabeza+1>=len(self.entrada):
                self.entrada.append(self.blanco)
            self.cabeza=self.cabeza+1
