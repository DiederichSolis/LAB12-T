import json

def calcular_potencia_lista(input_file, output_file, n):
    # Leer la lista de enteros desde el archivo de entrada
    with open(input_file, 'r') as file:
        lista = json.load(file)
    
    # Calcular la potencia n-ésima de cada elemento usando lambda
    resultado = list(map(lambda x: x ** n, lista))
    
    # Mostrar el resultado en la consola
    print(f"Lista original: {lista}")
    print(f"Lista elevada a la potencia {n}: {resultado}")
    
    # Guardar el resultado en el archivo de salida
    with open(output_file, 'w') as file:
        file.write(json.dumps(resultado))

# Parámetros
input_file = 'input.txt'        # Archivo de entrada
output_file = 'output.txt'      # Archivo de salida
n = 2                           # Potencia a aplicar

# Llamada a la función
calcular_potencia_lista(input_file, output_file, n)
