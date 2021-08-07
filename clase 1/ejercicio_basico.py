""" 
Ejercicio 3: 

  - Crear un programa que le pida ingresar 4 colores. 
  - Mostrarlos por consola.
  - Agregarle un color desde el programa, mostrarle al usuario el nuevo color agregado. 
  - imprimir la cantidad de colores. 
  - Pedirle al usuario que ingrese un nuevo color e insertarlo en la posición 1. Imprimir el    listado de colores.
  - Mostrale por consola al usuario el color que se encuentra en la posicion 3.
  - Eliminar el ultimo color de la lista.
  - Pedirle al usuario que ingrese un color para ver si existe en la lista, imprimir por consola True o False. 
  - Limpiar la lista e imprimirla por consola.
"""


""" 
    Alex - Niko 
                  """

# Mensaje al usuario
print("Este es mi programa de colores")
colores = input("Ingrese 4 colores: ")

# Impresion de colores
print(f"Sus colores son: {colores}")

# Al recibirlos como una cadena los podemos splitear por espacios
# este metodo nos devuelve una list
colores_lista = colores.split()
print(colores_lista)

# Agregamos un color a la lista
colores_lista.append('Negro')
print(colores_lista)

# logitud de la list
print("La cantidad de colores es: ", len(colores_lista))

# Le pedimos al usuario que ingrese un color
nuevo_color = input("Ingrese un nuevo color: ")
# Lo insertamos a la list
colores_lista.insert(1, nuevo_color)
print(colores_lista)

# Le mostramos al usuario el color de la posicion 3
print("El color que esta en la posicion 3 es: ", colores_lista[3])

# Quitamos el ultimo elemento de la list
# este metodo retorna el elemento
colores_lista.pop()
print(colores_lista)

# Le pedimos al usuario que nos indique un color a buscar en la list
buscar = input("Color a buscar: ")
# Devolvera True o False segun su existencia en la list
print(buscar in colores_lista)

# Limpiamos la list quitando todos sus elementos
colores_lista.clear()
print(colores_lista)


""" 
     Nacho - Fede - Eze 
                           """

""" color1 = input("Ingrese el primer color: ")
color2 = input("Ingrese el segundo color: ")
color3 = input("Ingrese el tercer color: ")
color4 = input("Ingrese el cuarto color: ")

print(f"Primer color: {color1}")
print(f"Segundo color: {color2}")
print(f"Tercer color: {color3}")
print(f"Cuarto color: {color4}")

lista = [color1, color2, color3, color4]

lista.append ("Cyan")

print("La cantidad de colores es: ", len(lista))

color5 = input("Ingrese un nuevo color: ")

lista.insert(1, color5)

print(lista[3])

lista.pop()

print(lista)

colorBusqueda = input("Ingrese un color para verificar si esta en la lista: ")

print(colorBusqueda in lista)

lista.clear()

print(lista) """


""" 
    Juampi - Perole - Rau 
                            """
""" 
colores = []
colores.insert(0, input("ingresar primer color: "))
# print(colores)
colores.append(input("ingresar cuarto color: "))
# print(colores)
colores.insert(1, input("ingresar segundo color: "))
# print(colores)
colores.insert(2, input("ingresar tercer color: "))
print(colores)
colores.append("marron")

print(colores)

print(len(colores))

colores.insert(0, input("ingresar nuevo color: "))
print(colores)

print(colores[2])

colores.pop()
print(colores)

color_para_buscar = input("buscar color: ")
print(color_para_buscar in colores)
#del colores
# colores.clear()
print(colores) """
