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
