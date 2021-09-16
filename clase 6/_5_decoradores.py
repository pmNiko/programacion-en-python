""" Creemos un decorador que contenga dos fn y se ejecuten segun
si el argumento que pasamos como parametro es True o False."""


def decorator(is_valid=False):
    def wrapper(function):

        def beforeAction():
            print("Antes de ejecutar la función.")

        def afterAction():
            print("Despues de ejecutar la función.")

        def wrapper2(*args, **kwargs):
            if is_valid:
                beforeAction()

            result = function(*args, **kwargs)
            afterAction()

            return result  # Retorna el resultado de la fn a decorar

        return wrapper2  # Retorna la segunda fn anidada

    return wrapper  # Retorna la funcion anidada


if __name__ == "__main__":
    @decorator(is_valid=True)
    def suma(numero_1, numero_2):
        return numero_1 + numero_2

    print(suma(2, 3))
