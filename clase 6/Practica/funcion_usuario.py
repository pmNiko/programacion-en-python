"""
  Ejercicio 1:
    Crear un archivo llamado funcion_usuario.py
    Generar una función que capture nombre y apellido de un usuario por consola
    y devuelva un mensaje por consola dando la bienvenida a dicho usuario, haciendo 
    de fstring y colorama imprimir el mensaje en color verde.
"""
from colorama import Fore, Style
from decoradores import logueado


@logueado
def login():
    """ La fn pide nombre y apellido separado por un espacio
    y devuelve un mensaje de bienvenida en color verde, por terminal."""
    datos = input("Ingrese su nombre y apellido: ").split()
    nombre, apellido = tuple(datos)
    print(Fore.GREEN, f'Bienvenido {nombre} {apellido}', Style.RESET_ALL)


if __name__ == '__main__':
    login()
