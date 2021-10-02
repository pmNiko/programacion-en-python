"""
  Ejercicio 4
  Localiza el error en el siguiente bloque de código. 
  Maneja la excepción para evitar que el programa se bloquee y 
  además explica en un mensaje al usuario la causa y/o solución:

    resultado = 15 + "20"
"""

while True:
    try: 
        numero = int(input("Ingrese un número: "))
        print(15 + numero)
        break
    except ValueError:
        print("Se debe ingresar un valor numérico, no una palabra.")
        
