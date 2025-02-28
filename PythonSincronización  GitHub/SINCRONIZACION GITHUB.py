def ordenar_fila(matriz, fila_a_ordenar):
    """
    Ordena una fila específica de una matriz bidimensional.

    Args:
        matriz: La matriz bidimensional.
        fila_a_ordenar: El índice de la fila que se va a ordenar.
    """
    fila = matriz[fila_a_ordenar]
    fila.sort() #Ordenamiento de manera ascendente.

# Matriz de ejemplo
matriz_ejemplo = [
    [9, 2, 7],
    [4, 5, 6],
    [1, 8, 3]
]

print("Matriz original:")
for fila in matriz_ejemplo:
    print(fila)

fila_a_ordenar = 0
ordenar_fila(matriz_ejemplo, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz_ejemplo:
    print(fila)