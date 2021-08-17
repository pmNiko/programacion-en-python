""" Definición de funciones """

# Definición generica
""" 
  def <nombreDeLaFuncion>(params?):
      <bloque de ejecución>
    """

# -------    fn decir hola   --------- #


def hola():
    print('Hola mundo!')


# Utilización de nuestra fn
# hola()


# -------    fn suma   --------- #
def suma(numero_1, numero_2):
    return numero_1 + numero_2


# resultado = suma(2, 2)
# print(resultado)


# -------    fn saludar usuario  --------- #
def holaUsuario(usuario):
    print(f'Bienvenido {usuario}')


# holaUsuario('Nikolas')


# -------    fn ver opcion   --------- #
def verOpcion(op):
    print(f'Usted eligio la opción {op}.')


# verOpcion(4)


# -------    fn saludar usuario  --------- #

def holaUsuario(nombre='invitado'):
    print(f'Bienvenido {nombre}!')


# holaUsuario()
# holaUsuario('Perole')


# -------    funciones en una linea --------- #
# fuente: https://www.freecodecamp.org/espanol/news/expresiones-lambda-en-python/

# def sumar(numero_1, numero_2: return numero_1 + numero_2

# sumar(50,30)


# def square(x): return x ** 2

# print(square(3))


# mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filtrado = filter(lambda x: x % 2 == 0, mi_lista)

# print(list(filtrado))


""" Por ultimo veamos que puede recibir una función """

# def miFuncion(argument, *args, **kwargs):
#     print(argument)
#     print(args)
#     print(kwargs)
#     print(type(argument), type(args), type(kwargs))
#     return argument, args, kwargs


# print(miFuncion(45, 32, 45, 67, "parameter", name="Martin", surname="paneblanco"))
