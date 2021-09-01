
from colorama import Fore,Style
import random
from datetime import datetime

def saludarUsuario():
    usuario = input('ingrese su nombre: ')
    print(Fore.GREEN)
    print(f'hola {usuario}.')
    print(Style.RESET_ALL)
    
def numeroAleatorio():
    numero_rand = random.randrange(1, 10)
    print(numero_rand)
    
def opcionElegida(op):
    print(f'opcion elegida {op}')




# Muestra la fecha actual
def fechaActual():
    '''Muestra la fecha actual'''
    now = datetime.now()
    format = now.strftime(f"\nLa fecha actual es: %d/%m/%Y")
    print(format)
    
# Login    
def credenciales():
    """ Recibe datos y los compara con alguno ya existente para hacer un login """
    username = "martin"    
    password = "martin111"
    
    if input("\nIngrese su UserName: ") == username and input("\nIngrese su password: ") == password:
        print("\nLogueado con exito!")
    else:
        print("\nError de credenciales")

# Calcula el area del rectangulo
def areaRectangulo():
    """ Recibe datos y calcula el area de un rectangulo """ 
    altura = int(input("\nIngrese la altura del rectangulo: "))
    largo = int(input("\nIngrese el largo del rectangulo: ")) 
    print("\nEl area del rectangulo es: " + str(largo * altura) + " cm2")

