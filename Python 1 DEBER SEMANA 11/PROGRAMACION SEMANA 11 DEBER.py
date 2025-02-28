def buscar_valor(matriz, valor_buscado):
    """
    Busca un valor en una matriz bidimensional.

    Args:
        matriz: La matriz bidimensional donde buscar.
        valor_buscado: El valor que se desea encontrar.

    Returns:
        Una tupla con la posición (fila, columna) si se encuentra, o None si no.
    """
    for fila_indice, fila in enumerate(matriz):
        for columna_indice, elemento in enumerate(fila):
            if elemento == valor_buscado:
                return fila_indice, columna_indice
    return None

# Matriz de ejemplo
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_a_buscar = 5
resultado = buscar_valor(matriz_ejemplo, valor_a_buscar)

if resultado:
    fila, columna = resultado
    print(f"El valor {valor_a_buscar} se encontró en la posición ({fila}, {columna}).")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")