"""
  Ejercicio 4
  Localiza el error en el siguiente bloque de código. 
  Maneja la excepción para evitar que el programa se bloquee y 
  además explica en un mensaje al usuario la causa y/o solución:

    resultado = 15 + "20"
"""
try:
    resultado = 15 + "20"
    
except TypeError:
    print("No podes sumar un dato de tipo str con otro de tipo int.")