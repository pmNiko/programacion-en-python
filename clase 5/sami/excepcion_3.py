"""
  Ejercicio 3
  Localiza el error en el siguiente bloque de código. 
  Maneja la excepción para evitar que el programa se bloquee y 
  además explica en un mensaje al usuario la causa y/o solución:

    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
    colores['blanco']
"""

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
try:
    colores['blanco']

except KeyError:
    print("La key ingresada no esta en el diccionario.")