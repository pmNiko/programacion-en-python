""" 
  Tipo de dato -> list
  """

#### Creacion #####
lista_de_items = [34, 'nombre', True, 30.5]
vocales = list('aeiou')

##### para imprimir por consola utilizamos la funcion print() ######
# print(lista_de_items)
# print(vocales)


# -------- 0    1    2    3  ----posiciones de ordenamiento
letras = ['A', 'B', 'G', 'K']

#### obtener un elemento especifico. Le pasamos la posicion entre corchetes ####
primer_elemento = letras[0]
print(primer_elemento)


##### Agregar un elemento a la lista en la posicion final ####
# letras.append('papa')
# print(letras)

##### Agregar un elemento a la lista en la posicion indicada ####
# letras.insert(1, 'J')
# print(letras)


##### Cambiar el contenido de una posicion en particular ####
letras[1] = 'mi nuevo contenido'
# print(letras)

##### Eliminar el ultimo elemento de la lista ####
letras.pop()
# print(letras)

##### Eliminar un elemento en particular de la lista ####
letras.remove('A')
# print(letras)

##### Vaciar la lista ####
letras.clear()
# print(letras)

##### Eliminar la lista ####
# del letras
# print(letras)


""" 
  Prueben los siguientes metodos e imprimanlos por consola
    """

numeros = [90, 20, 40, 89, 20, 4, 90, 20]

# print(20 in numeros)
# print(202 not in numeros)
# print(id(numeros))
# numeros.sort()
# print(numeros)
# numeros.sort(reverse=True)
# print(numeros)
# print(id(numeros))
# print(numeros.count(20))
# print(len(numeros))
