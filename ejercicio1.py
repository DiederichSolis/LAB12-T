import json

def ordenar_diccionarios_por_key(input_file, output_file, key):
    # Leer el archivo de entrada
    with open(input_file, 'r') as file:
        data = json.load(file)  # Cargar la lista de diccionarios desde el archivo

    # Ordenar la lista según la clave especificada
    data_sorted = sorted(data, key=lambda x: x[key])

    # Mostrar el resultado en consola
    print("Lista ordenada por la clave '{}':".format(key))
    for item in data_sorted:
        print(item)

    # Guardar el resultado en el archivo de salida
    with open(output_file, 'w') as file:
        for item in data_sorted:
            file.write(json.dumps(item) + '\n')

# Parámetros
input_file = 'data.txt'         # Archivo de entrada
output_file = 'sorted_output.txt'  # Archivo de salida
key = 'model'                     # Clave por la cual ordenar

# Llamada a la función
ordenar_diccionarios_por_key(input_file, output_file, key)
