import cinta as Cinta
import MT
import transicion as Transicion
import Js as JS
import sys

class Menu:
    
    x = open(sys.argv[1])
    j = JS.JsonUwU(x)
    switch = False
    i = 0
    cadena = sys.argv[2]
    if (len(cadena) == 1):
        if cadena in j.entrada:
            switch = True
    else:
        for x in cadena:
            if (x in j.entrada):
                i+=1
                if(i == len(cadena)-1):
                    switch = True
    if(switch):
        c = Cinta.cinta(list(cadena),j.blanco)
        t = Transicion.trancision(j.transiciones)
        mt = MT.MaquinaTuring(j.estados,j.entrada,c,j.inicial,j.blanco,j.finales,t)
        i = 0
        print("Las configuraciones son : ")
        aux = " "
        print("| " + mt.estadoActual + " | " + aux.join(mt.cinta.entrada)) #No se si sea necesario poner la configuracion inicial, pero esta es una forma fea de que lo haga
        while (i == 0):
            i = mt.mover()
            print("| " + mt.estadoActual + " | " + aux.join(mt.cinta.entrada)) #La idea es que imprima el estado y la cadena en cada paso
        if(i == -1):
            print("No es aceptada")
        else:
            print("Es aceptada")
    else:
        print("Esa cadena no es valida")
