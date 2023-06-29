#codigo principal
import os
import time
import numpy as np
import funciones_gato as gt
from random import choice
borrar=gt.borrarpantalla(os.name)
fichaX="X"
fichaO="O"
c=chr(27)+"[1;33m"
n=chr(27)+"[0;37m"
v=chr(27)+"[1;32m"
try:
    while True:
        print(v+" ")
        print("\nBienvenido a Gato 3000 \n")
        print("Seleccione una opcion:")
        print("\n 1.-Jugador Vs. Jugador \n 2.-Jugador Vs. CPU \n 0.- Salir ")
        print(n+"")
        opcion=gt.filtrar_op(0,2)
        os.system(borrar)
        if opcion==0:
            os.system(borrar)
            print("Cerrando Aplicaccion \nGracias por jugar")
            time.sleep(2)
            os.system(borrar)
            break
        elif opcion==1:
            jugador1=""
            jugador2=""
            fj1=""
            fj2=""
            jugador1,fj1,jugador2,fj2=gt.definir_jugadores(fichaX,fichaO)
            while True:
                gt.JvJ(jugador1,fj1,jugador2,fj2)
                print("REVANCHA??? \n 1.- SI            2.- NO")
                opcion=gt.filtrar_op(1,2)
                if opcion==1:
                    print("iniciando REVANCHA... \n el orden de inicio se invertira")
                    jugador1,jugador2=jugador2,jugador1
                    pause=input("precione cualquier tecla para continuar : \n")
                    os.system(borrar)
                else:
                    print("Volviendo al menu Principal...")
                    pause=input("precione cualquier tecla para continuar : \n")
                    os.system(borrar)
                    break
        elif opcion==2:
            jugador1=""
            jugador2=""
            fj1=""
            fj2=""
            jugador1,fj1,jugador2,fj2=gt.definir_jugadores(fichaX,fichaO,True)
            while True:
                gt.JvC(jugador1,fj1,jugador2,fj2)
                print("REVANCHA??? \n 1.- SI            2.- NO")
                opcion=gt.filtrar_op(1,2)
                if opcion==1:
                    print("iniciando REVANCHA... \n el orden de inicio se invertira")
                    jugador1,jugador2=jugador2,jugador1
                    pause=input("precione cualquier tecla para continuar : \n")
                    os.system(borrar)
                else:
                    print("Volviendo al menu Principal...")
                    pause=input("precione cualquier tecla para continuar : \n")
                    os.system(borrar)
                    break
except:
    print("mensaje de error")