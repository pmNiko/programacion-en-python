""" 
   Diferencia entre return y yield"""


# ----- Return retorna un elemento y corta la ejecución de la fn

def unaFuncion(una_lista):
    for ele in una_lista:
        return ele


# contenemos en la variable la devolucion de la funcion
devolucion = unaFuncion(range(1, 10))

# Al imprimir la devolucion podemos ver que solo nos ha devuelto
# el primer elemento
print(devolucion)


# ---- Hagamos el mismo proceso con yield

def otraFuncion(una_lista):
    for ele in una_lista:
        yield ele


# contenemos en la variable la devolucion de la funcion
retorno = otraFuncion(range(1, 10))

# Al imprimir la devolucion podemos ver que nos devuelve
# un objeto generador
print(retorno)

# Entonces pasemoslo como parametro de una función list()
print(list(retorno))
# bien, de esta manera vemos que nos ha devuelto todos los elementos
