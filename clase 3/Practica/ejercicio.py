
from funciones import saludarUsuario, numeroAleatorio, opcionElegida, fechaActual, credenciales, areaRectangulo




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
        opcionElegida(opcion)
    elif opcion == 4:
        fechaActual()
    elif opcion == 5:
        credenciales()
    elif opcion == 6:
        areaRectangulo()
    elif opcion == 7:
        print("Saliendo del sistema...")
    else:
        print("Opción invvalida.")
