"""
  Ejercicio 1
  Localiza el error en el siguiente bloque de código. 
  Maneja la excepción para evitar que el programa se bloquee y 
  además explica en un mensaje al usuario la causa y/o solución:

  resultado = 10/0
"""
try:
  resultado = 10/0 

except ZeroDivisionError:
  print("No podes dividir por cero. Reintentar")
  