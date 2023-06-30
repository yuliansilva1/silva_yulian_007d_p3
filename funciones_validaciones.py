#----------------------------------------------------
import os
#validacion del menu colocar las opciones requeridas y la canidad
def validar_menu():
    os.system('cls')
    print("""MENÚ
    1.rut
    2.nombre
    3.coreo
    4.descuento
    5.edad
    6.genero
    7.salir""")

#validacion de opciones recordar cambiar el in dependiendo del numero del menu    
def validar_opcion():
    while True:
        try:
            opc = int(input("Ingrese opcion: "))
            if opc in(1,2,3,4,5,6,):
                return opc
            else:
                print("Opcion invalida")
        except:
            print("ERROR! debe ingresar un numero")
            
#validacion de rut entre 10000000 y 99999999 cambiar si es requerido
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if rut >= 10000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR rut entre 10000000 y 99999999")
        except:
            print("ERROR! debe ingresar un numero entero")
            
#validacion de nombre con largo 3 y sin espacio y solo letras
def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR debe tener al menos 3 letras")
            
#validacion de correo con @
def validar_correo():
    while True:
        correo = input("Ingrese correo: ")
        if "@gmail" or "@hotmail" or "outlook" in correo:
            return correo
        else:
            print("ERROR correo incorrecto")
            
#cambiar el 100 para conseguir el tope si no es un descuento fijo
def validar_descuento():
    while True:
        try:
            descuento = int(input("Ingrese descuento: "))
            if descuento >= 0 and descuento <= 100:
                return descuento
            else:
                print("ERROR descuento entre 0 y 100")
        except:
            print("ERROR! debe ingresar un numero entero")
            
#validacion de la edad entre 0 y 100 cambiar si es requerido
def validar_edad():
    while True:
        try:
            edad = int(input("Ingrese edad(entre 0 y 100): "))
            if edad >= 0 and edad <= 100:
                return edad
            else:
                print("ERROR edad fuera de rango de 0 y 100")
        except:
            print("ERROR! debe ingresar un numero entero")
            
#validacion del genero para que sea F,M,O
def validar_genero():
    while True:
        genero = input("Ingrese genero(f: femenino, m: masculino, o: otro): ")
        if genero.upper() in ("F","M","O"):
            return genero
        else:
            print("ERROR el genero debe ser F,M,O")
        
