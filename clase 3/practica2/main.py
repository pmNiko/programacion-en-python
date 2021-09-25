""" importacion de modulos """
# from funciones import suma
import random
from funciones import saludoUsuario
from funciones import numeroAleatorio
from funciones import opcionElegida
menu=   """ Menu
  1- Saludar usuario
  2- Mostrar un numero aleatorio
  3- Mostrar opcion elegida
  4- Ver fecha actual
  5- Login de usuario
  6- Area de un rectangulo
  7- Salir """
  
print(menu)

while True: 
    opcion= int(input("ingrese una opcion: "))
    
    if opcion == 1: 
        """ pedirle el nomre, saludarlo escribiendo el nombre ingresado, """
        # suma()
        nombre= input("ingrese su nombre: ")
        
        saludoUsuario(nombre)
    
    elif opcion == 2: 
        # print(random.randint(0, 10))
       numeroAleatorio()
    elif opcion == 3: 
        opcionElegida(opcion)
    
    elif opcion == 4: 
        pass
    
    elif opcion == 5: 
        pass
    
    elif opcion == 6: 
        pass
    
    elif opcion == 7: 
        print("Saliendo del sistema.")
        break
    
    else:
        print("Opcion no valida.")