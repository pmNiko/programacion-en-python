""" Generemos un switch con un diccionario y funciones"""

# importación del modulo random y datetime
import random
import datetime

# -------    Definición de funciones  --------- #


# Función para saludar al usuario
def saludarUsuario():
    usuario = input('Ingrese su nombre: ')
    print(f'\n\tBienvenido al sistema {usuario}\n')


# Función que muetra un número random entre 1-10
def mostrarUnNumero():
    numero = random.randrange(1, 10)
    print(f"\n\tEste es un numero random {numero}\n")


# Imprime que se ha elegido la opción tes
def login():
    __nick = "usuario123"
    __password = "123456"
    nick = input('Ingrese su nombre: ')
    password = input('Ingrese su contraseña: ')

    if __nick == nick and __password == password:
        print("\n\tLogueado con éxito!\n")
    else:
        print("\n\tError en las credenciales.\n")


# Función para mostrar la fecha actual
def fecha():
    fecha_sin_formatear = datetime.datetime.now()
    # Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S
    fecha = fecha_sin_formatear.strftime('%d/%m/%Y')
    print(f"\n\tFecha actual -> {fecha}\n")


# Calcular el area de un cuadrado
def areaDeUnCuadrado():
    lado = float(input("Ingrese la medida de un lado: "))
    area = round((lado * 2), 2)
    print(f'\n\tEl area de su cuadrado es {area}\n')


# definamos el diccionario de opciones
opciones = {
    1: saludarUsuario,
    2: mostrarUnNumero,
    3: login,
    4: fecha,
    5: areaDeUnCuadrado
}

# Menu de opciones
menu = """ 
  Menu
  1- Saludar usuario
  2- Mostrar un numero
  3- Login
  4- Ver fecha
  5- Area de un cuadrado
  6- Salir
"""

# Le mostramos el menu al usuario
print(menu)

# Bandera de corte
continuar = True
# Bucle while
while continuar:
    # opción numerica del usuario
    opcion = int(input('Ingrese la opción: '))
    # Valor de la clave
    accion = opciones.get(opcion)

    # Switch de acciones
    if opcion == 6:
        print('\n\tSaliendo del sistema...\n')
        continuar = False
    elif accion == None:
        print("Opción incorrecta\n\n")
    else:
        accion()
