"""
  Ejercicio 1
  Localiza el error en el siguiente bloque de código. 
  Crea una excepción para evitar que el programa se bloquee y 
  además explica en un mensaje al usuario la causa y/o solución:

  resultado = 10/0
"""

# try:
#     resultado = 10 / 0
# except ZeroDivisionError:
#     print("No se puede dividir por 0.")


"""
  Ejercicio 2
  Localiza el error en el siguiente bloque de código. 
  Crea una excepción para evitar que el programa se bloquee y 
  además explica en un mensaje al usuario la causa y/o solución:

    lista = [1, 2, 3, 4, 5]
    lista[10]
"""
# try:
#     lista = [1, 2, 3, 4, 5]
#     lista[10]
# except IndexError:
#     print("El indice de la lista al que esta intentando acceder no existe.")


"""
  Ejercicio 3
  Localiza el error en el siguiente bloque de código. 
  Crea una excepción para evitar que el programa se bloquee y 
  además explica en un mensaje al usuario la causa y/o solución:

    colores = { 'rojo':'red', 'verde':'green', 'negro':'black' } 
    colores['blanco']
"""
# try:
#     colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
#     colores['blanco']
# except KeyError:
#     print("La clave que esta intentando recuperar no esta contenida en el diccionario.")


"""
  Ejercicio 4
  Localiza el error en el siguiente bloque de código. 
  Crea una excepción para evitar que el programa se bloquee y 
  además explica en un mensaje al usuario la causa y/o solución:

    resultado = 15 + "20"
"""
# try:
#     resultado = 15 + "20"
# except TypeError:
#     print("No se puede conccatenar un int con un str.")


"""
  Ejercicio 5
  Realiza una función llamada agregarUnaVez(lista, elemento) que reciba una lista y un elemento. 
  La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
  Además si este elemento ya se encuentra en la lista se debe invocar 
  un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

  Error: Imposible añadir elementos duplicados => [elemento].

  Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" 
  y luego muestra su contenido.

  --- Sugerencia ---

  Puedes utilizar la sintaxis "elemento in lista"

  --> lista inicial:  
          elementos = [1, 5, -2]

"""


# def agregarUnaVez(una_lista: list, elemento):
#     if elemento in una_lista:
#         raise ValueError(
#             {"msg": f"Error: Imposible añadir elementos duplicados => [{elemento}]."})
#     una_lista.append(elemento)


# elementos = [1, 5, -2]

# try:
#     agregarUnaVez(elementos, 10)

#     agregarUnaVez(elementos, -2)

#     agregarUnaVez(elementos, "Hola")
# except ValueError as err:
#     detalle = err.args[0]
#     print(detalle["msg"])

# for index, ele in enumerate(elementos):
#     print(f"Indice: {index} => elemento: {ele}")

# Podemos ver que al dispararse la excepción ya no se sigue ejecutando
# el resto del bloque de codigo indentado al try, por esto es que
# no se ve el elemento "Hola"
