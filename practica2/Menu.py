import cinta as Cinta
import MT
import transicion as Transicion
import Js as JS
import sys

class Menu:
    
    x = open(sys.argv[1])
    j = JS.JsonUwU(x)
    switch = True
    cadena = sys.argv[2]
    if (len(cadena) == 1):
        switch = cadena in j.entrada
    else:
        for x in cadena:
            if (x not in j.entrada):
                switch=False
    if(switch):
        c = Cinta.cinta(list(cadena),j.blanco,j.inicial)
        t = Transicion.trancision(j.transiciones)
        mt = MT.MaquinaTuring(j.estados,j.entrada,c,j.inicial,j.blanco,j.finales,t)
        i = 0
        print("Las configuraciones son : ")
        while (i == 0):
            print(c) #La idea es que imprima el estado y la cadena en cada paso
            i = mt.mover()
        if(i == -1):
            print("No es aceptada")
        else:
            print("Es aceptada")
    else:
        print("Esa cadena no es valida")
