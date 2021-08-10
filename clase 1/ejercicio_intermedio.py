
""" Ejercicio 2:

  Crear un menu de usuario con las siguientes opciones:
    - 1 mostrar un numero
    - 2 mostrar una frase
    - 3 mostrar opción seleccionada
    - 4 salir del sistema
  pista: utilizar while - if elif else """

print("""
    - 1 mostrar un numero
    - 2 mostrar una frase
    - 3 mostrar opción seleccionada
    - 4 salir del sistema 
        """)

#  Tomi - Perole - Fede
""" opcion = 0

while opcion != 4:
    opcion = int(input("Ingrese opcion: "))

    if opcion == 1:
        print(56)
    elif opcion == 2:
        print("Esta es una frase.")
    elif opcion == 3:
        print(f"Usted selecciono la opcion {opcion}")
    elif opcion == 4:
        print("saliendo del sistema...")
    else:
        print("Opcion incorrecta.") """


# Rau - Nacho -Juli - Juampi
lista = [input("Ingrese el primer número: "), input(
    "Ingrese el segundo número: "), input("Ingrese el tercer número: ")]

# Solución 1
# if (lista[0] == lista[1] and lista[0] == lista[2]):
#     print("\nLos 3 números son iguales")
# elif(lista[0] == lista[1] or lista[0] == lista[2] or lista[1] == lista[2]):
#     print("\n2 números son iguales")
# else:
#     print("\nLos números no son iguales")


# Solución 2
numeros = set(lista)

if len(numeros) == 1:
    print("Todos sus elementos son iguales")
elif len(numeros) == 2:
    print("2 elementos son iguales")
else:
    print("Todos los elementos son distintos")
