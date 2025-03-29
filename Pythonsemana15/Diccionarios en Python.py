# Crear un Diccionario
informacion_personal = {
    "nombre": "Edinson Romero",
    "edad": 39,
    "ciudad": "Machala",
    "profesion": "Ingeniero Agronomo"
}

# Acceder y Modificar Valores
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")
informacion_personal["ciudad"] = "Orellana"
print(f"Ciudad modificada: {informacion_personal['ciudad']}")

# Verificar Existencia de Claves y Agregar
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0981464419"
    print("Se agregó la clave 'telefono'.")
else:
    print("La clave 'telefono' ya existe.")

# Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("Se eliminó la clave 'edad'.")
else:
    print("La clave 'edad' no existe en el diccionario.")

# Imprimir el Diccionario Final
print("\nDiccionario final:")
print(informacion_personal)