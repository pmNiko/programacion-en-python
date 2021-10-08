"""
  Ejercicio 2:
    Crear un modulo llamado decoradores.py
    Definir un decorador llamado: @logueado
    dicho decorador debe mostrar fecha y hora cuando el usuario esta intentando loguearse, haciendo uso 
    del modulo datetime capture la fecha y hora muestrela por consola antes de ejecutar 
    la función que recibe como parametro, luego de ejecutar la función decorada debe 
    imprimir un mensaje por consola que diga gracias por ingresar. 
    Por ultimo en el archivo de funcion_usuario.py importe el decorador y apliquelo a
    la definición de dicha función para comprobar su correcto funcionamiento.
    
"""
from datetime import datetime


def logueado(func):
    """ Decorador para capturar fecha y hora de login. """
    def wrapper():
        now = datetime.now()
        format = now.strftime(f"\nLa fecha actual es: %d/%m/%Y %H:%M hs")
        print(format)

        func()

        print("\nGracias por ingresar!")

    return wrapper


# -------- Ejercicio 3 -------------- #
""" Una vez que tengamos funcionando nuestra funcion correctamente, en el modulo decoradores.py
    definir un nuevo decorador llamado "logueado_2" que nos permita recibir una función con parametros.  """


def logueado_2(func):
    """ Decorador para capturar fecha y hora de login. """
    def wrapper(*args, **kwargs):
        now = datetime.now()
        format = now.strftime(f"\nLa fecha actual es: %d/%m/%Y %H:%M hs")
        print(format)

        func(*args, **kwargs)

        print("\nGracias por ingresar!")

    return wrapper


# -------- Ejercicio 5 -------------- #
"""
    Ejercicio 5:
    Dentro del modulo decoradores.py definir un nuevo decorador llamado @connect
    el cual debe imprimir un mensaje: 
            "Conección a base de datos activa..."
    antes de ejecutar la fn decorada y un mensaje: 
            "Conección a la base de datos cerrada."
    luego de ejecutar la fn decorada.

"""


def connect(func):
    """ Decorador encargado de abrir y cerrar la conexion a la BD. """
    def wrapper(*args, **kwargs):
        print("Conección a base de datos activa...")

        func(*args, **kwargs)

        print("Conección a la base de datos cerrada.")

    return wrapper


# -------- Ejercicio 6 -------------- #
"""
    Ejercicio 6:
    Dentro del modulo decoradores.py definir un nuevo decorador llamado @connect_2(autorized=False)
    el cual extendera la funcionalidad del decorador connect para que en el caso de recibir autorized=True
    ejecutará la funcionalidad anterior, pero en caso contrario lanzará una excepción ValueError con 
    un msg indicando que no tiene permiso para realizar la acción que esta intentando efectuar.
    
    Por ultimo importarla en el modulo verduleria, quitar @connect y decorar la fn agregarFruta() 
    con @connect_2(), y luego pasarle autorized=True como parametro para ver su funcionamiento.

"""


def connect_2(autorized=False):
    """ Decorador encargado de abrir y cerrar la conexion a la BD. """
    def wrapper(func):
        def wrapper2(*args, **kwargs):
            if autorized:
                print("Conección a base de datos activa...")

                func(*args, **kwargs)

                print("Conección a la base de datos cerrada.")
            else:
                raise ValueError(
                    {"msg": "Usted no tiene permiso para realizar la acción que esta intentando efectuar."})

        return wrapper2
    return wrapper
