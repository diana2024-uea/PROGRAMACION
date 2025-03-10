import random

# Dimensiones de la matriz
ciudades = ["Orellana", "Sucumbios", "Napo"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]

# Crear la matriz 3D
temperaturas = [[[random.uniform(10, 30) for _ in dias] for _ in semanas] for _ in ciudades]

# Calcular y mostrar promedios
for i, ciudad in enumerate(ciudades):
    for j, semana in enumerate(semanas):
        promedio_semanal = sum(temperaturas[i][j]) / len(dias)
        print(f"Promedio en {ciudad}, {semana}: {promedio_semanal:.2f} grados")