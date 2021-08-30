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


# resultado = suma(2, 200)
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
# holaUsuario('Ruben')
