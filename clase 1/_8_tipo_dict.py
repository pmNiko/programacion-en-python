""" 
    Tipo Dict
  """

# 1. Pares clave: valor encerrados entre llaves
dict_1 = {'uno': 1, 'dos': 2, 'tres': 3}
# print(dict_1)

# 2. Argumentos con nombre
dict_2 = dict(uno=1, dos=2, tres=3)
# print(dict_2)

# 3. Pares clave: valor encerrados entre llaves
dict_3 = dict({'uno': 1, 'dos': 2, 'tres': 3})
# print(dict_3)

# 4. Iterable que contiene iterables con dos elementos
dict_4 = dict([('uno', 1), ('dos', 2), ('tres', 3)])
# print(dict_4)

# 5. Diccionario vacío
dict_5 = {}
# print(dict_5)

# 6. Diccionario vacío usando el constructor
dict_6 = dict()
# print(dict_6)


""" Acceder a los elementos """
# print(dict_1['uno'])
# print(dict_1.get('uno'))

# Devuelve 4 como valor por defecto si no encuentra la clave
# print(dict_1.get('cuatro', 4))

# Devuelve None como valor por defecto si no encuentra la clave
a = dict_1.get('cuatro')
# print(type(a))


""" Recorrer los elementos """

# recorrer las claves
# for key in dict_1:
#     print(key)


# recorrer las claves
# for key in dict_1.keys():
#     print(key)


# recorrer los valores
# for value in dict_1.values():
#     print(value)

# recorrer clave-valor
# for ele in dict_1.items():
#     print(ele)


""" Añadir elementos """

# este tambien aplica a modificación de claves
# dict_1['cinco'] = 5
# print(dict_1)

# setdefault asigna un elemento si no existe
# dict_1.setdefault('seis', 6)
# print(dict_1)

# elemento_existente = dict_1.setdefault('seis', 10)
# print(elemento_existente)
# print(dict_1)

""" Borrar elementos """
#  se puede utilizar pop o del
# indicando el elemento

dict_1.pop('dos')
print(dict_1)

del dict_1['tres']
print(dict_1)
