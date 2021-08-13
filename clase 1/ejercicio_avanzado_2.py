
# Ejercicio 2

# Creación de la coleccion
frutas = {'Banana': 100.50, 'Manzana': 80.90, 'Pera': 75.20, 'Naranja': 50.25}

# Impresión de las frutas disponibles
print('\t"Fruta"   "Precio por kilo"')
for fruta in frutas:
    print(f'\t{fruta}     \t${frutas[fruta]}')


# Ingreso de datos del usuario
fruta = input('¿Qué fruta quieres? ').capitalize()
kg = float(input('¿Cuántos kilos? '))

# Existencia de la fruta elegida por el usuario
""" if fruta in frutas:
    # calculo del precio por kg
    precio = frutas[fruta]
    total = precio * kg
    print(f'{kg} kilos de {fruta} cuestan ${total}.')
else:
    print("Lo siento, la fruta", fruta, "no está disponible.") """


# B Agregar la fruta que no existe
if fruta in frutas:
    # calculo del precio por kg
    precio = frutas[fruta]
    total = precio * kg
    print(f'{kg} kilos de {fruta} cuestan ${total}.')
else:
    print("Lo siento, la fruta", fruta, "no está disponible")
    respuesta = input('Desea agregarla si - no: ')
    if respuesta == 'si':
        precio_fruta = float(input('Ingrese el precio: '))
        frutas.setdefault(fruta, precio_fruta)

        # Impresión de las frutas disponibles
        print('\t"Fruta"   "Precio por kilo"')
        for fruta in frutas:
            print(f'\t{fruta}     \t${frutas[fruta]}')
    else:
        print('La fruta no ha sido agregada.')
