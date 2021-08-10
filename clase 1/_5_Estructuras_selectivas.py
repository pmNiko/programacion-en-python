""" 
  Estructuras selectivas 
  """

# operadores de comparacion
# > mayor que
# >= mayor o igual que
# < menor que
# <= menor o igual que
# == igual que
# != distinto que
# condiciones and, or y not

# if 2 > 1:
#     print("2 es mayor que 1")

# if 2 >= 1:
#     print("2 es mayor o igual que 1")

# if 2 < 3:
#     print("2 es menor que 3")

# if 2 <= 3:
#     print("2 es menor o iguel que 3")

# if 3 == 3:
#     print("3 es igual a 3")

# if 3 != 4:
#     print("3 es ditinto a 4")

# if not 3 == 4:
#     print("3 no es igual a 4")

# if 2 < 3 and 4 > 3:
#     print("Ambas condiciones son true.")

# if 2 > 3 or 4 > 3:
#     print("Una o ambas condiciones son verdaderas.")


""" Tabla de verdad """

""" condicion and """

# condicion-A     condicion-B     Resultado
#     T               T               T
#     T               F               F
#     F               F               F
#     F               T               F


""" condicion or """

# condicion-A     condicion-B     Resultado
#     T               T               T
#     T               F               T
#     F               F               F
#     F               T               T


""" Selectiva if else 
  """

# if 2 >= 5:
#     print("La condición es verdadera")
# else:
#     print("La condición es falsa!")


""" Selectiva if elif else 
    Con este se puede simular un switch
  """
if 2 > 3:
    print("Se cumple la primera condición.")
elif 2 < 3:
    print("Se cumple la segunda condición.")
else:
    print("No se cumplio ninguna de las condiciones.")
