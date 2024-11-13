import json

def calcular_transpuesta(input_file, output_file):
    # Leer la matriz desde el archivo de entrada
    with open(input_file, 'r') as file:
        matriz = json.load(file)
    
    # Calcular la transpuesta usando zip y lambda
    transpuesta = list(map(lambda *row: list(row), *matriz))
    
    # Mostrar la matriz transpuesta en consola
    print("Matriz transpuesta:")
    for fila in transpuesta:
        print(fila)
    
    # Guardar la matriz transpuesta en el archivo de salida
    with open(output_file, 'w') as file:
        file.write(json.dumps(transpuesta))

# Parámetros
input_file = 'matrix.txt'            # Archivo de entrada
output_file = 'transposed_matrix.txt'  # Archivo de salida

# Llamada a la función
calcular_transpuesta(input_file, output_file)
