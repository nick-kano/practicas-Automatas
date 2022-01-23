class cinta:
    cabeza=0

    def __init__(self,entrada,blanco,estado):
        self.entrada=entrada
        self.blanco=blanco
        self.estadoActual=estado
    
    def leer(self):
        return self.entrada[self.cabeza]

    def transicion(self,estado,escribir,mover):
        self.estadoActual=estado
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
    
    def __str__(self):
        aux=""
        for x in range(len(self.entrada)):
            if x == self.cabeza:
                aux = aux+"|" + self.estadoActual + "|"
            aux = aux + " " + self.entrada[x]+ " "
        return aux