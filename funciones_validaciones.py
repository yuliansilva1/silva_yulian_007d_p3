import os
import time
import numpy
habitacion = numpy.zeros((2,5), int)
def mostrar_menu():
    os.system('cls')
    print("""Menú
    1. Grabar
    2. Buscar
    3. Retirarse
    4.salir""")

def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opcion: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! DEBE ESCOGER UNA OPCION VALIDA")
        except:
            print("ERROR! DEBE ESCOGER UN NUMERO ENTERO")


def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni digito verificador): "))
            if rut >= 10000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR rut entre 10000000 y 99999999")
        except:
            print("ERROR! debe ingresar un numero entero")

def validacion_nombre_d():
    while True:
        nombre_d = input("Ingrese su nombre: ")
        if len(nombre_d.strip()) >= 3 and nombre_d.isalpha():
            return nombre_d
        else:
            print("ERROR debe tener al menos 3 letras")

def mensaje_despedida():
    print("GRACIAS POR VISITAR MASCOTA SEGURA")
    time.sleep(3)
def validacion_nombre_m():
    while True:
        nombre_m = input("Ingrese nombre mascota: ")
        if len(nombre_m.strip()) >= 3 and nombre_m.isalpha():
            return nombre_m
        else:
            print("ERROR debe tener al menos 3 letras")

def validacion_dias():
    try:
        dias = int(input("ingrese dias de hospedaje: "))
        if dias >= 1:
            return dias
        else:
            print("debe ingresar una cantidad mayor a 1")
    except:
        print("ERROR debe ingresar un numero entero")

def pagar():
    print("su total a pagar es xxxxxxx")
    time.sleep(3)

def ver_habitacion():
    os.system('cls')
    print("\tVER RESTAURANT\n")
    contador = 1
    for x in range(2):
        print(f" {(x+1)}: ",end=" ")
        for y in range(5):
            print(f" {contador}: {habitacion[x][y]} ", end=" ")
            contador += 1
        print("\n")
    time.sleep(3)
