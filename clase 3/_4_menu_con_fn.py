""" Generemos un switch con un funciones """

# importación del modulo random y datetime
import random
import datetime

# -------    Definición de funciones  --------- #


def saludarUsuario():
    usuario = input('Ingrese su nombre: ')
    print(f'Bienvenido {usuario}')


def mostrarUnNumero():
    print(random.randrange(1, 10))


def verOpcion(op):
    print(f'Usted eligio la opción {op}.')


def fecha():
    fecha_sin_formatear = datetime.datetime.now()
    # Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S
    fecha = fecha_sin_formatear.strftime('%d/%m/%Y')
    print(fecha)


def salirDelSistema():
    print('Saliendo del sistema.')
    return False


# Menu de opciones
menu = """ 
  Menu
  1- Saludar usuario
  2- Mostrar un numero
  3- Mostrar opcion
  4- Ver fecha
  5- Salir
"""

# Le mostramos el menu al usuario
print(menu)


# Bandera de corte
continuar = True
# Bucle while
while continuar:
    # opción numerica del usuario
    opcion = input('Ingrese la opción: ')

    # Switch de opciones
    if opcion == '1':
        saludarUsuario()
    elif opcion == '2':
        mostrarUnNumero()
    elif opcion == '3':
        verOpcion(opcion)
    elif opcion == '4':
        fecha()
    elif opcion == '5':
        continuar = salirDelSistema()
    else:
        print('Opción incorrecta.')
