import time


def calcular_tiempo(function):
    """ Decodador para calcular el tiempo de ejecución """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        print('Tiempo total: ', time.time() - start)

        return result  # Retorna el resultado de la fn decorada

    return wrapper


if __name__ == '__main__':

    @calcular_tiempo
    def suma(numero_1, numero_2):
        time.sleep(3)
        return numero_1 + numero_2

    print(suma(3, 9))
