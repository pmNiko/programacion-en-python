"""
  Ejercicio 2
  Localiza el error en el siguiente bloque de código. 
  Maneja la excepción para evitar que el programa se bloquee y 
  además explica en un mensaje al usuario la causa y/o solución:

    lista = [1, 2, 3, 4, 5]
    lista[10]
"""

while True:
    lista = [1, 2, 3, 4, 5] 
    try: 
        numero_lista = int(input("Ingrese el número del rango de la lista: "))
        print(lista[numero_lista])
        break
    except IndexError:
        print("El valor ingresado está fuera del rango de la lista.")