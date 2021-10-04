"""
  Ejercicio 3:
    Crear un modulo llamado login_user.py
    Vamos a redefinir la funcion login que creamos en el modulo funcion_usuario.py
    para que ahora reciba como parametro nombre y apellido, realizando la misma salida
    por consola que hacia anteriormente(por ahora sin decorador).
    Una vez que tengamos funcionando nuestra funcion correctamente, en el modulo decoradores.py
    definir un nuevo decorador llamado "logueado_2" que nos permita recibir una función con parametros.
    Una vez hecha la definicion de nuestro nuevo decorador capaz de soportar fn con parametros, importarlo
    en el modulo login_user.py y decorar la funcion para comprobar su funcionamiento. 
    
"""

from colorama import Fore, Style
from decoradores import logueado_2


@logueado_2
def login(nombre: str, apellido: str):
    """ La fn recibe nombre y apellido como parametro
    y devuelve un mensaje de bienvenida en color verde, por terminal."""

    print(Fore.GREEN, f'Bienvenido {nombre} {apellido}', Style.RESET_ALL)


if __name__ == '__main__':
    datos = input("Ingrese su nombre y apellido: ").split()
    nombre, apellido = tuple(datos)
    login(nombre, apellido)
