"""
  Ejercicio 5
  Realiza una función llamada agregarUnaVez(lista, elemento) tal que reciba una lista y un elemento. 
  La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
  Además si este elemento ya se encuentra en la lista se debe invocar 
  un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

  Error: Imposible añadir elementos duplicados => [elemento].

  Cuando tengas la función intenta añadir los siguiente valores a la lista: 10, -2, "Hola" 
  y luego muestra su contenido.

  --- Sugerencia ---

  Puedes utilizar la sintaxis "elemento in lista"

  --> lista inicial:  
          elementos = [1, 5, -2]

"""
listita = [1, 5, -2]

def agregarUnaVez(lista: list, elemento: int): 
    if elemento in lista: 
      raise ValueError("Error: Imposible añadir elementos duplicados => [" + str(elemento) + "].")
    lista.append(elemento)
    
try:
  agregarUnaVez(listita, 4) 
    
except ValueError as err:
  print(err)  

print(listita)
 


