""" Generemos un switch con un diccionario """

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

# definamos el diccionario de opciones
opciones = {
    1: "Hola usuario",
    2: 999,
    3: "Usted eligio la opcion 3",
    4: "14/08/2021",
    5: False
}

# Bandera de corte
continuar = True
# Bucle while
while continuar:
    # opción numerica del usuario
    opcion = int(input('Ingrese la opción: '))
    # Valor de la clave
    valor = opciones.get(opcion)

    # Switch de acciones
    if opcion == 5:
        continuar = valor
        print('Saliendo del sistema.')
    elif valor == None:
        print("Opción incorrecta")
    else:
        print(valor)
