# Para que el decorador pueda recibir los N argumentos
# vamos a trabajar con *args, **kwargs
# para que nuestra fn retorne el resultado debemos devolverlo
def decorador_custom(fn_a_decorar):
    """ Decorador recibe los params que puede llegar a 
    necesitar nuestra función a decorar, luego se almacena
    en una variable la cual sera retornada."""

    def nuevaFuncion(*args, **kwargs):
        print("Vamos a ejecutar la fn")
        resultado = fn_a_decorar(*args, **kwargs)
        print("Se ejecuto la fn")

        return resultado

    # devolvemos la nueva función decorada
    return nuevaFuncion


if __name__ == '__main__':

    # ----- uso del nuevo decorador ------- #
    @decorador_custom
    def suma(numero_1, numero_2):
        return numero_1 + numero_2

    print(suma(10, 20))
