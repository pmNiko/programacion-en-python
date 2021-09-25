from random import random
import random

def login():
    usuario = "usuario123"
    password = "1234"
    

    nombre = input("Ingrese su Nick : ")
    clave = input("ingrese su clave : ")
    
    
    if  usuario == nombre and password == clave :
         print("logeado con exito")
    else : 
        print("Nombre incorrecto")





def saludoUsuario(un_nombre):
    print("Hola", un_nombre, "como estas?")
    
def numeroAleatorio():
     print("el numero aleatorio es: ", random.randrange(5,21))
    
def opcionElegida(opcion):
    print("opcion seleccionada: ", opcion)

