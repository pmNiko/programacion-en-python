""" Los errores de sintaxis son los mas comunes cuando estamos 
conociendo un nuevo lenguaje."""

# Fuente: https://docs.python.org/es/3/tutorial/errors.html

# while True print("Hola mundo")
# El interprete marca la linea en la cual se produce el
# el error y arroja el mensaje SintaxError: invalid sintax

""" Errores semanticos: estos se dan cuando a pesar de terner 
una sintaxis correcta el programa no tiene un resultado esperado"""
# numeros = [1, 2, 3, 4, 0]
# numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(numeros_pares)
# Por consola podemos ver que ha tomado entre los numeros pares al 0
# Podemos mejorar nuestra condicion
# numeros_pares = list(filter(lambda x: x % 2 == 0 and x != 0, numeros))
# print(numeros_pares)


""" Errores de ejecucion, estos aparecen en runtime y pueden producir 
cortes de ejecucion, lanzando excepciones no manejadas.
    Veamos como manejar excepciones."""

# Por consola probemos ingresar: Este es un String
# while True:
#     numero = int(input("Ingrese un numero: "))
# print("Fin del programa...")
# ValueError: invalid literal for int() with base 10: 'Este es un String'
# Podemos ver como se corta la ejecucion de nuestro programa

""" Excepcion:  ValueError 
    El interprete arroja una excepción al tratar de castear un string, 
    y corta la ejecución del programa. Pero podemos manejarla con la 
    sentencia try except
"""

# Por consola probemos ingresar: Este es un String
# while True:
#     try:
#         numero = int(input("Ingrese un numero: "))
#         break
#     except ValueError:
#         print("Debe ingresar un numero, vuelva a intentarlo.")
# print("Fin del programa...")
# Con esta sentencia cubrimos el caso de que el usuario ingrese
# mal el dato por consola, si el bloque dentro de try arroja una excepcion
# será capturada y manejada por except de los contrario se ejecutará y
# continuará con la ejecucion del programa.


""" Excepcion:  ZeroDivisionError
    El interprete arroja una excepción al tratar de dividir por 0.
"""
# Por consola probemos ingresar: 0
# while True:
#     dividendo = 10
#     try:
#         divisor = int(input("Ingrese un divisor: "))
#         cociente = dividendo / divisor
#         print(f"""El cociente de la division:
#               => {dividendo} / {divisor}
#               => Cociente: {cociente}""")
#         break
#     except ZeroDivisionError:
#         print("Debe ingresar un numero distinto de 0, vuelva a intentarlo.")
#     except ValueError:
#         print("Debe ingresar un numero, vuelva a intentarlo.")
# print("Fin del programa...")


""" Excepcion:  NameError
    El interprete arroja una excepción al tratar de acceder a una variable 
    que no ha sido declarada.
"""

# try:
#     variable_no_definida + 3

# except NameError:
#     print("Esta intentando acceder a una variable no definida.")
# print("La ejecucion del programa continua porque hemos manejado la excepción")


""" Excepcion:  TypeError
    El interprete arroja una excepción al tratar de concatenar un string 
    con un int.
"""
# try:
#     '3' + 3
# except TypeError:
#     print("No se pude concateenar un str con un tipo int.")
# print("La ejecucion del programa continua porque hemos manejado la excepción")


""" Como propagar una excepcion """

# try:
#     raise NameError
# except NameError:
#     print("Usted ha propagado una excepción.")


""" Incluso podemos pasarle información del error """

# try:
#     raise NameError({"mensaje": "La variable no ha sido encontrada."})
# except NameError as err:
#     detalle = err.args[0]
#     print(detalle["mensaje"])
