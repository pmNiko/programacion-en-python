from funciones import saludarUsuario, numeroAleatorio

""" Ejercicio en grupo """

menu = """ 
      Menu
  1- Saludar usuario
  2- Mostrar un numero aleatorio
  3- Mostrar opcion elegida
  4- Ver fecha actual
  5- Login de usuario
  6- Area de un rectangulo
  7- Salir
"""

print(menu)

opcion = 0

while opcion != 7:
    opcion = int(input("Ingrese una opción: "))
    # Saludar usuario
    if opcion == 1:
       saludarUsuario()
    # Numero aleatorio
    elif opcion == 2:
        numeroAleatorio()
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass
    elif opcion == 7:
        print("Saliendo del sistema...")
    else:
        print("Opción invvalida.")
