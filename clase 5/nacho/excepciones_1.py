"""
  Ejercicio 1
  Localiza el error en el siguiente bloque de código. 
  Maneja la excepción para evitar que el programa se bloquee y 
  además explica en un mensaje al usuario la causa y/o solución:

  resultado = 10/0
"""


while True:
    dividendo = 10 
    try: 
      divisor = int(input("Ingrese el número divisor: "))
      cociente = dividendo / divisor
      print(cociente)
      break
    except ZeroDivisionError:
        print("El valor 0 no es reconocible") 

# try:
#   resultado = 10/0
# except ZeroDivisionError:
#   print("No se puede dividir por 0.")