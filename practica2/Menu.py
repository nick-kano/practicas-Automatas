import cinta
import MT
import transicion
import Js


class Menu:

    json = js()
    switch = False
    while switch == False: #revisa que la cadena si tenga los simbolos que aceptamos
        i = 0
        cadena = input("Favor de ingresar la cadena de entrada")
        for x in cadena:
            if not(x in json.cinta):
                print("Esa cadena no es valida, favor de ingresar una que lo sea")
                break
            else:
                i+=1
                if(i == cadena.length()-1):
                    switch = true

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

