import tkinter as tk
from PIL import Image, ImageTk

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Visualización de Imágenes")

# Función para cargar y mostrar una imagen
def mostrar_imagen(nombre_archivo):
    # Abrir la imagen con PIL
    imagen = Image.open(nombre_archivo)
    # Convertir la imagen para Tkinter
    imagen_tk = ImageTk.PhotoImage(imagen)
    # Crear un label que contenga la imagen
    label_imagen.config(image=imagen_tk)
    label_imagen.image = imagen_tk  # mantener referencia
    # Actualizar texto
    label_texto.config(text="Universidad Estatal Amazónica")

# Label para mostrar la imagen
label_imagen = tk.Label(ventana)
label_imagen.pack()

# Label para mostrar el texto
label_texto = tk.Label(ventana, text="", font=("Arial", 16))
label_texto.pack()

# Botón para cargar una imagen específica (ejemplo con imagen 1)
boton_cargar = tk.Button(
    ventana, 
    text="Mostrar Imagen 1", 
    command=lambda: mostrar_imagen("Imagenes/IMAGEN (1).png")
)
boton_cargar.pack()

ventana.mainloop()