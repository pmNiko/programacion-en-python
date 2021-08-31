from datetime import datetime

def fechaActual():
    now = datetime.now()
    format = now.strftime(f"\nLa fecha actual es: %d/%m/%Y")
    print(format)
    
def credenciales():
    username = "martin"    
    password = "martin111"
    
    if input("\nIngrese su UserName: ") == username and input("\nIngrese su password: ") == password:
        print("\nLogueado con exito!")
    else:
        print("\nError de credenciales")

def areaRectangulo(): 
    altura = int(input("\nIngrese la altura del rectangulo: "))
    largo = int(input("\nIngrese el largo del rectangulo: ")) 
    print("\nEl area del rectangulo es: " + str(largo * altura) + " cm2")
