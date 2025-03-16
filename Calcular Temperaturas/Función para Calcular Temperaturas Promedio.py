def calcular_temperatura_promedio(temperaturas, ciudades):
    """
    Calcula la temperatura promedio de cada ciudad durante un período de tiempo.

    Args:
        temperaturas (list): Lista de listas de listas de diccionarios con datos de temperatura.
        ciudades (list): Lista con los nombres de las ciudades.

    Returns:
        dict: Diccionario con el promedio de temperatura para cada ciudad.
    """
    promedios_por_ciudad = {}

    for ciudad_index, ciudad in enumerate(temperaturas):
        suma_total = 0
        total_dias = 0

        for semana in ciudad:
            for dia in semana:
                suma_total += dia['temp']
                total_dias += 1

        if total_dias > 0:
            promedio_ciudad = suma_total / total_dias
            promedios_por_ciudad[ciudades[ciudad_index]] = round(promedio_ciudad, 2)
        else:
            promedios_por_ciudad[ciudades[ciudad_index]] = "Sin datos"

    return promedios_por_ciudad

# Datos de temperatura para Napo, Sucumbíos y Orellana
temperaturas = [
    [  # Napo
        [  # Semana 1
            {"dia": "Lunes", "temp": 24},
            {"dia": "Martes", "temp": 25},
            {"dia": "Miércoles", "temp": 23},
            {"dia": "Jueves", "temp": 26},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 24},
            {"dia": "Domingo", "temp": 26}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 23},
            {"dia": "Martes", "temp": 24},
            {"dia": "Miércoles", "temp": 25},
            {"dia": "Jueves", "temp": 24},
            {"dia": "Viernes", "temp": 26},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 23}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 26},
            {"dia": "Martes", "temp": 25},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 23},
            {"dia": "Viernes", "temp": 24},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 26}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 25},
            {"dia": "Martes", "temp": 26},
            {"dia": "Miércoles", "temp": 23},
            {"dia": "Jueves", "temp": 24},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 26},
            {"dia": "Domingo", "temp": 23}
        ]
    ],
    [  # Sucumbíos
        [  # Semana 1
            {"dia": "Lunes", "temp": 27},
            {"dia": "Martes", "temp": 28},
            {"dia": "Miércoles", "temp": 26},
            {"dia": "Jueves", "temp": 29},
            {"dia": "Viernes", "temp": 28},
            {"dia": "Sábado", "temp": 27},
            {"dia": "Domingo", "temp": 29}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 26},
            {"dia": "Martes", "temp": 27},
            {"dia": "Miércoles", "temp": 28},
            {"dia": "Jueves", "temp": 27},
            {"dia": "Viernes", "temp": 29},
            {"dia": "Sábado", "temp": 28},
            {"dia": "Domingo", "temp": 26}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 29},
            {"dia": "Martes", "temp": 28},
            {"dia": "Miércoles", "temp": 27},
            {"dia": "Jueves", "temp": 26},
            {"dia": "Viernes", "temp": 27},
            {"dia": "Sábado", "temp": 28},
            {"dia": "Domingo", "temp": 29}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 28},
            {"dia": "Martes", "temp": 29},
            {"dia": "Miércoles", "temp": 26},
            {"dia": "Jueves", "temp": 27},
            {"dia": "Viernes", "temp": 28},
            {"dia": "Sábado", "temp": 29},
            {"dia": "Domingo", "temp": 26}
        ]
    ],
    [  # Orellana
        [  # Semana 1
            {"dia": "Lunes", "temp": 25},
            {"dia": "Martes", "temp": 26},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 27},
            {"dia": "Viernes", "temp": 26},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 27}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 24},
            {"dia": "Martes", "temp": 25},
            {"dia": "Miércoles", "temp": 26},
            {"dia": "Jueves", "temp": 25},
            {"dia": "Viernes", "temp": 27},
            {"dia": "Sábado", "temp": 26},
            {"dia": "Domingo", "temp": 24}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 27},
            {"dia": "Martes", "temp": 26},
            {"dia": "Miércoles", "temp": 25},
            {"dia": "Jueves", "temp": 24},
            {"dia": "Viernes", "temp": 25},
            {"dia": "Sábado", "temp": 26},
            {"dia": "Domingo", "temp": 27}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 26},
            {"dia": "Martes", "temp": 27},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 25},
            {"dia": "Viernes", "temp": 26},
            {"dia": "Sábado", "temp": 27},
            {"dia": "Domingo", "temp": 24}
        ]
    ]
]

ciudades = ["Napo", "Sucumbíos", "Orellana"]

resultado = calcular_temperatura_promedio(temperaturas, ciudades)
print(resultado)