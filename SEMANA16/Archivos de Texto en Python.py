# Escritura de Archivo de Texto
try:
    # Abre el archivo my_notes.txt en modo escritura ('w').
    # Si el archivo no existe, se crea. Si existe, su contenido se sobrescribe.
    with open("my_notes.txt", "w") as archivo_escritura:
        # Escribe tres líneas de notas personales en el archivo.
        archivo_escritura.write("Esta es la primera nota sobre mi.\n")
        archivo_escritura.write("Hoy aprendí como trabajar archivos en Python.\n")
        archivo_escritura.write("Debo  practicar  regularmente los temas vistos en clases.\n")
    print("Se han escrito las notas en el archivo my_notes.txt")

except Exception as e:
    print(f"Ocurrió un error al escribir en el archivo: {e}")

# Lectura de Archivo de Texto
try:
    # Abre el archivo my_notes.txt en modo lectura ('r').
    with open("my_notes.txt", "r") as archivo_lectura:
        print("\nContenido del archivo my_notes.txt:")
        # Lee el archivo línea por línea utilizando readline().
        linea = archivo_lectura.readline()
        while linea:
            # Muestra cada línea leída en la consola, eliminando el salto de línea al final.
            print(linea.strip())
            linea = archivo_lectura.readline()

except FileNotFoundError:
    print("El archivo my_notes.txt no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")

# Cierre de Archivos
# El uso de 'with open(...)' asegura que los archivos se cierren automáticamente
# al salir del bloque 'with', incluso si ocurren errores.
# No es necesario llamar a archivo.close() explícitamente en este caso.

print("\nOperaciones de lectura y escritura completadas.")