""" importacion de modulos """
# from funciones import suma
from funciones import login
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
        # suma()
        pass
    
    elif opcion == 2: 
        pass
    
    elif opcion == 3: 
        pass
    
    elif opcion == 4: 
        pass
    
    elif opcion == 5: 
        login()
    
    elif opcion == 6: 
        pass
    
    elif opcion == 7: 
        print("Saliendo del sistema.")
        break
    
    else:
        print("Opcion no valida.")