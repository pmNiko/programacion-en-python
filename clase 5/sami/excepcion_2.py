"""
  Ejercicio 2
  Localiza el error en el siguiente bloque de código. 
  Maneja la excepción para evitar que el programa se bloquee y 
  además explica en un mensaje al usuario la causa y/o solución:

    lista = [1, 2, 3, 4, 5]
    lista[10]
"""

lista = [1, 2, 3, 4, 5]
x= 1
while x != 0:
  try:
      i= input("ingrese una posicion: ")
      lista[int(i)]
      print(lista[int(i)])
      
  except IndexError:
      print("No se encontro el elemento en la posicion", i)
      x= 0
      