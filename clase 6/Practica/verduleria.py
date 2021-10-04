"""
  Ejercicio 4:
    Crear un modulo llamado verduleria.py
    - Definir una variable frutas y asignarle una lista de frutas: 
          -Naranja  -Kiwi  -Frutilla  -Banana  -Manzana 

    - Definir una función agregarFruta(una_fruta, lista_de_frutas) que tome una fruta como parametro 
      y la agregue a la lista. 

    - Genenrar una excepción ValueError() con un msg indicando el error, para
      contener el caso de que la fruta que esta intentando agregar ya exista en la colección.

    - Probar su funcionamiento manejando la excepción y finalmente imprimiendo el listado de frutas.

      agregarFruta('pera', frutas)
      agregarFruta('manzana', frutas)

"""
from decoradores import connect, connect_2

# @connect


@connect_2()
def agregarFruta(una_fruta: str, lista_de_frutas: list):
    if una_fruta.lower() in map(str.lower, lista_de_frutas):
        raise ValueError(
            {"msg": f"Error: Imposible añadir elementos duplicados => [{una_fruta}]."})
    lista_de_frutas.append(una_fruta.capitalize())


if __name__ == '__main__':
    frutas = ['Naranja', 'Kiwi', 'Frutilla', 'Banana', 'Manzana']
    try:
        agregarFruta('pera', frutas)
        agregarFruta('manzana', frutas)
    except ValueError as err:
        detalle = err.args[0]
        print(detalle["msg"])

    print(frutas)
