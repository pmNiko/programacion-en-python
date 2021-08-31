""" Documentación de funciones """


def cuadradoDeUnNumero(numero: int) -> int:
    """ Toma como parametro un numero y lo eleva al cuadrado """
    return numero ** 2


# resultado = cuadradoDeUnNumero(5)
# print(resultado)


def imprimirTabla(usuarios: dict):
    """ Toma como parametro una colección de usuarios de tipo dict
    con clave: nombre y value: apellido y lo  imprime en formato tabla """
    print(f'\tNombre\t\tApellido')
    for key, value in usuarios.items():
        print(f'\t{key}\t\t{value}')


# usuarios = {'Nicola': 'Tesla', 'Juan': 'Baustista', 'Pedro': 'Juarez'}
# imprimirTabla(usuarios)


""" # -------    fn con parametros nombrados --------- # """


def misDatos(nombre='Nikolas', edad=32, dni='34.220.535'):
    print(f'Soy {nombre} tengo {edad} y mi DNI es {dni}')


# misDatos()
# misDatos('Juan', 28, '43.435.980')
# misDatos(edad=33)


""" Por ultimo veamos que puede recibir una función """

# def miFuncion(argument, *args, **kwargs):
#     print(argument)
#     print(args)
#     print(kwargs)
#     print(type(argument), type(args), type(kwargs))
#     return argument, args, kwargs


# print(miFuncion(45, 32, 45, 67, "parameter", name="Martin", surname="paneblanco"))
