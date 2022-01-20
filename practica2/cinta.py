class cinta:
    cabeza=0

    def __init__(self,entrada):
        self.entrada=entrada
    

    def leer(self):
        return entrada[cabeza]

    def trancisionValida(self,simbolo):
        return simbolo==leer()

    def trancision(leido,escribir,mover):
        if trancisionValida(leido):
            entrada[cabeza]=escribir
            if mover=="L":
                if cabeza==0:
                    entrada.insert(0,"_")
                else:
                   cabeza=cabeza-1
            else:
                if cabeza+1>=len(entrada):
                    entrada.append("_")
                cabeza=cabeza+1
            return 1
        else:
            return -1