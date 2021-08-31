from colorama import Fore,Style
import random

def saludarUsuario():
    usuario = input('ingrese su nombre: ')
    print(Fore.GREEN)
    print(f'hola {usuario}.')
    print(Style.RESET_ALL)
    
def numeroAleatorio():
    numero_rand = random.randrange(1, 10)
    print(numero_rand)