import cinta
import MT
import transicion
import Js as JS
import sys

class Menu:
    
    j = JS.JsonUwU(sys.argv[1])
    switch = False
    i = 0
    cadena = sys.argv[2]
    for x in cadena:
        if (x in j.cinta):
            i+=1
            if(i == cadena.length()-1):
                switch = true
    if(switch == true):
        c = Cinta(cadena,json.blanco)
        t = Transicion(json.transicion)
        mt = MaquinaTuring(json.estados,json.entrada,c,json.inicial,json.finales,json.blanco,t)
        i = 0
        print("Las configuraciones son : ")
        print("| " + mt.estadoActual + " | " + mt.cinta.entrada) #No se si sea necesario poner la configuracion inicial, pero esta es una forma fea de que lo haga
        while (i == 0):
            i = mt.mover()
            print("| " + mt.estadoActual + " | " + mt.cinta.entrada) #La idea es que imprima el estado y la cadena en cada paso
        if(i == -1):
            print("No es aceptada")
        else:
            print("Es aceptada")
    else:
        print("Esa cadena no es valida")
