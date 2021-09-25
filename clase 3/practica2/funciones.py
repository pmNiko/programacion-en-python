def login():
  
    usuario = "usuario123"
    password = "1234"
    
    nombre = input("Ingrese su Nick : ")
    clave = input("ingrese su clave : ")
    
    
    if  usuario == nombre and password == clave :
         print("logeado con exito")
    else : 
        print("Nombre incorrecto")
