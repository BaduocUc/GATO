import random
import os
import numpy as np

def borrarpantalla(name):
    if name=="posix":
        borrar="clear"
        return borrar    
    elif name=="ce" or name=="nt" or name=="dos":
        borrar="cls"
        return borrar    
    
def filtrar_op(min,max):
    v=chr(27)+"[1;32m"
    n=chr(27)+"[0;37m"
    while True:
        try:
            op=int(input())
            if op<min or op>max:
                print(v+"Opcion Invalida... Intentelo nuevamente",n+"")
            else:
                return op
        except:
            print(v+"Caracter Invalida... Intentelo nuevamente",n+"")
            
def matrizgato():
    libre=["1","2","3","4","5","6","7","8","9"]
    gato=np.array([["1","2","3"],["4","5","6"],["7","8","9"]])
    return gato,libre
            
def ganador(matriz,fichaj):
    v=chr(27)+"[1;32m"
    n=chr(27)+"[0;37m"
    if   matriz[0,0]==fichaj and matriz[0,1]==fichaj and matriz[0,2]==fichaj:
        print(v+"GANO GANO GANO ...",n+"")
        return True
    elif matriz[1,0]==fichaj and matriz[1,1]==fichaj and matriz[1,2]==fichaj:
        print(v+"GANO GANO GANO ...",n+"")
        return True
    elif matriz[2,0]==fichaj and matriz[2,1]==fichaj and matriz[2,2]==fichaj:
        print(v+"GANO GANO GANO ...",n+"")
        return True
# gana con fila
    elif matriz[0,0]==fichaj and matriz[1,0]==fichaj and matriz[2,0]==fichaj:
        print(v+"GANO GANO GANO ...",n+"")
        return True
    elif matriz[0,1]==fichaj and matriz[1,1]==fichaj and matriz[2,1]==fichaj:
        print(v+"GANO GANO GANO ...",n+"")
        return True
    elif matriz[0,2]==fichaj and matriz[1,2]==fichaj and matriz[2,2]==fichaj:
        print(v+"GANO GANO GANO ...",n+"")
        return True
# gana con columnas
    elif matriz[0,0]==fichaj and matriz[1,1]==fichaj and matriz[2,2]==fichaj:
        print(v+"GANO GANO GANO ...",n+"")
        return True
    elif matriz[0,2]==fichaj and matriz[1,1]==fichaj and matriz[2,0]==fichaj:
        print(v+"GANO GANO GANO ...",n+"")
        return True
#gana con diagonales

def definir_jugadores(fichaX,fichaO,COM=False):
    v=chr(27)+"[1;32m"
    n=chr(27)+"[0;37m"
    borrar=borrarpantalla(os.name)
    print(v+" ")
    j1=input("\nIngrese el Nombre/Apodo del 1º Jugador\n")
    if COM==False:
        j2=input("\nIngrese el Nombre/Apodo del 2º Jugador\n")
    else:
        j2="MAQUINA"
    while j1.upper()==j2.upper():
        print("los nombre de cada jugador deben ser distintos \n...intente nuevamente")
        j1=input("\nIngrese Nombre/Apodo del 1º Jugador\n")
        if COM==False:
            j2=input("\nIngrese Nombre/Apodo del 2º Jugador\n")
        else:
            j2="MAQUINA"
    while True:
        try:
            ficha=int(input(f"Jugador {j1} escoga su ficha:\n 1.- X             2.- O\n"))
            while ficha not in [1,2]:
                print("Opcion Invalida... Intentelo nuevamente")
                ficha=int(input(f"Jugador {j1} escoga su ficha:\n 1.- X             2.- O\n"))
            print(n+"")
            os.system(borrar)
            if ficha==1:
                j1ficha=fichaX
                j2ficha=fichaO
            else:
                j1ficha=fichaO
                j2ficha=fichaX
            return j1,j1ficha,j2,j2ficha
        except:
            print(v+"Caracter Invalida... Intentelo nuevamente",n+" ")
            
            
def JvJ(j1,fichaj1,j2,fichaj2):
    matriz,libres=matrizgato()
    borrar=borrarpantalla(os.name)
    c=chr(27)+"[1;33m"
    n=chr(27)+"[0;37m"
    v=chr(27)+"[1;32m"
    switch=True   
    resultado=False
    jugador=""
    ficha=""
    while True:
        try:
            print(n+" ")
            print("┏━━━┳━━━┳━━━┓")
            print("┃",c+matriz[0,0],n+"┃",c+matriz[0,1],n+"┃",c+matriz[0,2],n+"┃")
            print("┣━━━╋━━━╋━━━┫")
            print("┃",c+matriz[1,0],n+"┃",c+matriz[1,1],n+"┃",c+matriz[1,2],n+"┃")
            print("┣━━━╋━━━╋━━━┫")
            print("┃",c+matriz[2,0],n+"┃",c+matriz[2,1],n+"┃",c+matriz[2,2],n+"┃")
            print("┗━━━┻━━━┻━━━┛ \n")
            resultado=ganador(matriz,ficha)
            if len(libres)==0:
                print(v+"empate",n+"")
                break
            elif resultado:
                print(v+"FELICIDADES AL JUGADOR ",jugador," POR SU VICTORIA")
                break
            elif switch:
                jugador=j1
                ficha=fichaj1
            elif switch==False:
                jugador=j2
                ficha=fichaj2
            print(v+"Turno de ",jugador,"\n")
            opcion=(input("escoga la casilla a ocupar:  "))
            while opcion not in libres:
                print("casilla ocupada o fuera de rango... intentelo nuevamente")
                opcion=(input("escoga la casilla a ocupar:  "))
            libres.remove(opcion)
            for i in range(3):
                for j in range(3):
                    if matriz[i,j]==opcion:
                        matriz[i,j]=ficha
                        os.system(borrar)
            switch = not switch
        except:
            print(v+"opcion invalida",n+"")
            
def CPU_FACIL(disponibles):
    selec=random.choice(disponibles)
    return selec

def CPU_CPU(matriz,disponibles,ficha,dificultad):
    if dificultad in ["NORMAL","DIFICIL"]:
        for i in range (3):
            for j in range (3):
                if matriz[i,j] in disponibles:
                    if matriz[i,j-1]==ficha and matriz[i,j-2]==ficha:
                        selec=matriz[i,j]
                        return selec
                    if matriz[i-1,j]==ficha and matriz[i-2,j]==ficha:
                        selec=matriz[i,j]
                        return selec
                    if matriz[i,j] in ["1","3","5","7","9"]:
                        if matriz[i-1,j-2]==ficha and matriz[i-2,j-1]==ficha:
                            selec=matriz[i,j]
                            return selec                      
    if dificultad == "DIFICIL":
        if ficha=="O":
            enemy="X"
        if ficha=="X":
            enemy="O"
        for i in range (3):
            for j in range (3):
                if matriz[i,j] in disponibles:
                    if matriz[i,j-1]==enemy and matriz[i,j-2]==enemy:
                        selec=matriz[i,j]
                        return selec
                    if matriz[i-1,j]==enemy and matriz[i-2,j]==enemy:
                        selec=matriz[i,j]
                        return selec
                    if matriz[i,j] in ["1","3","5","7","9"]:
                        if matriz[i-1,j-2]==enemy and matriz[i-2,j-1]==enemy:
                            selec=matriz[i,j]
                            return selec               
    selec=random.choice(disponibles)
    return selec

def choise_dificultad():
    facil="FACIL"
    normal="NORMAL"
    dificil="DIFICIL"
    print("Seleccione la Dificultad del combate ")
    print(F"1.-{facil}     2.-{normal}     3.-{dificil} ")
    selec=filtrar_op(1,3)
    if selec==1:
        return facil
    if selec==2:
        return normal
    if selec==3:
        return dificil


def JvC(j1,fichaj1,CPU,fichaj2):
    dificultad=choise_dificultad()
    matriz,libres=matrizgato()
    borrar=borrarpantalla(os.name)
    c=chr(27)+"[1;33m"
    n=chr(27)+"[0;37m"
    v=chr(27)+"[1;32m"
    switch=True
    if j1=="MAQUINA":
        switch=False
        j1,CPU=CPU,j1
    resultado=False
    jugador=""
    ficha=""
    while True:
        try:
            print(n+" ")
            print("┏━━━┳━━━┳━━━┓")
            print("┃",c+matriz[0,0],n+"┃",c+matriz[0,1],n+"┃",c+matriz[0,2],n+"┃")
            print("┣━━━╋━━━╋━━━┫")
            print("┃",c+matriz[1,0],n+"┃",c+matriz[1,1],n+"┃",c+matriz[1,2],n+"┃")
            print("┣━━━╋━━━╋━━━┫")
            print("┃",c+matriz[2,0],n+"┃",c+matriz[2,1],n+"┃",c+matriz[2,2],n+"┃")
            print("┗━━━┻━━━┻━━━┛ \n")
            resultado=ganador(matriz,ficha)
            if len(libres)==0:
                print(v+"empate",n+"")
                break
            elif resultado:
                print(v+"FELICIDADES AL JUGADOR ",jugador," POR SU VICTORIA")
                break
            elif switch:
                jugador=j1
                ficha=fichaj1
            elif switch==False:
                jugador=CPU
                ficha=fichaj2
            print(v+"Turno de ",jugador,"\n")
            if jugador==CPU:
                print(f"TURNO DE LA {jugador}")
                opcion=CPU_CPU(matriz,libres,ficha,dificultad)
            if jugador==j1:
                opcion=(input("escoga la casilla a ocupar:  "))
            while opcion not in libres:
                print("casilla ocupada o fuera de rango... intentelo nuevamente")
                opcion=(input("escoga la casilla a ocupar:  "))
            libres.remove(opcion)
            for i in range(3):
                for j in range(3):
                    if matriz[i,j]==opcion:
                        matriz[i,j]=ficha
                        if jugador==CPU:
                            print("LA ",jugador," OCUPO EL ESPACIO ",opcion,)
                            pause=input("precione cualquier tecla para continuar : \n")
                        os.system(borrar)
            switch = not switch
        except:
            print(v+"opcion invalida",n+"")