def eliminar_elementos(lista_inicial, elementos_a_borrar):
    # Usar filter y lambda para crear una lista con los elementos que no están en la lista de elementos a borrar
    lista_resultante = list(filter(lambda x: x not in elementos_a_borrar, lista_inicial))
    return lista_resultante

# Listas de ejemplo
lista_inicial = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
elementos_a_borrar = [ 'café', 'blanco']

# Llamada a la función y mostrar resultado
resultado = eliminar_elementos(lista_inicial, elementos_a_borrar)
print("Lista resultante:", resultado)
