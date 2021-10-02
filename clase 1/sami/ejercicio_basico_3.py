""" Ejercicio 3: 

  - Crear un programa que le pida ingresar 4 colores. 
  - Mostrarlos por consola.
  - Agregarle un color desde el programa, mostrarle al usuario el nuevo color agregado. 
  - imprimir la cantidad de colores. 
  - Pedirle al usuario que ingrese un nuevo color e insertarlo en la posición 1. Imprimir el listado de colores.
  - Mostrale por consola al usuario el color que se encuentra en la posicion 3.
  - Eliminar el ultimo color de la lista.
  - Pedirle al usuario que ingrese un color para ver si existe en la lista, imprimir por consola Verdadero o Falso. 
  - Limpiar la lista e imprimirla por consola. """
  
colores = input("ingrese 4 colores: ")
colores_split = colores.split()
print(colores_split) 
# print(type(colores_split))

print("elementos de la lista: ")
for elemento  in colores_split:
    print(f"elemento: {elemento}")



""" colores_split.append("e")
print(colores_split)

print(len(colores_split))

colores_split.insert(1, "z")
print(colores_split)

color_posicion = colores_split[3]
print(color_posicion) 

colores_split.pop()
print(colores_split)

color_extra = input("ingrese un color a buscar: ")
print(color_extra in colores_split)

colores_split.clear()
print(colores_split)
 """