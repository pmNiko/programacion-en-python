"""
  Ejercicio 3
  Localiza el error en el siguiente bloque de código. 
  Maneja la excepción para evitar que el programa se bloquee y 
  además explica en un mensaje al usuario la causa y/o solución:

    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
    colores['blanco']
"""


while True:
    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }  
    try: 
        color_dicc = input("Ingrese un color del diccionario: ")
        print(colores[color_dicc])
        break
    except KeyError:
        print("El color ingresado no está ingresado en el diccionario.")