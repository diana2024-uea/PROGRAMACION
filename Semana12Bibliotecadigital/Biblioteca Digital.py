import json
import os

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.info[0]}' por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

    def to_dict(self):
        return {
            "titulo": self.info[0],
            "autor": self.info[1],
            "categoria": self.categoria,
            "isbn": self.isbn
        }

    @staticmethod
    def from_dict(data):
        return Libro(data["titulo"], data["autor"], data["categoria"], data["isbn"])


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de objetos Libro

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

    def to_dict(self):
        # Guardamos solo los ISBN de los libros prestados para evitar duplicar datos
        return {
            "nombre": self.nombre,
            "id_usuario": self.id_usuario,
            "libros_prestados": [libro.isbn for libro in self.libros_prestados]
        }

    @staticmethod
    def from_dict(data, libros_dict):
        usuario = Usuario(data["nombre"], data["id_usuario"])
        # Reconstruimos la lista de libros prestados a partir de los ISBN
        for isbn in data.get("libros_prestados", []):
            libro = libros_dict.get(isbn)
            if libro:
                usuario.libros_prestados.append(libro)
        return usuario


class Biblioteca:
    def __init__(self):
        self.libros = {}    # isbn -> Libro
        self.usuarios = {}  # id_usuario -> Usuario

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.info[0]}' añadido.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            # Antes de eliminar, quitar el libro de los usuarios que lo tengan prestado
            for usuario in self.usuarios.values():
                usuario.libros_prestados = [libro for libro in usuario.libros_prestados if libro.isbn != isbn]
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print("ID de usuario ya registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = self.usuarios.get(id_usuario)
        if not libro:
            print("Libro no disponible.")
            return
        if not usuario:
            print("Usuario no registrado.")
            return
        if libro in usuario.libros_prestados:
            print("El usuario ya tiene este libro prestado.")
            return
        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, isbn, id_usuario):
        usuario = self.usuarios.get(id_usuario)
        if not usuario:
            print("Usuario no registrado.")
            return
        libro = self.libros.get(isbn)
        if libro and libro in usuario.libros_prestados:
            usuario.libros_prestados.remove(libro)
            print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
        else:
            print("El usuario no tiene este libro prestado.")

    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            titulo, autor = libro.info
            if criterio == "titulo" and valor.lower() in titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() == libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_prestados(self, id_usuario):
        usuario = self.usuarios.get(id_usuario)
        if not usuario:
            print("Usuario no registrado.")
            return []
        return usuario.libros_prestados

    def listar_todos_los_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            print("Libros disponibles en la biblioteca:")
            for libro in self.libros.values():
                print(libro)

    def guardar_datos(self, libros_file="libros.json", usuarios_file="usuarios.json"):
        # Guardar libros
        with open(libros_file, "w", encoding="utf-8") as f:
            json.dump([libro.to_dict() for libro in self.libros.values()], f, indent=4, ensure_ascii=False)
        # Guardar usuarios
        with open(usuarios_file, "w", encoding="utf-8") as f:
            json.dump([usuario.to_dict() for usuario in self.usuarios.values()], f, indent=4, ensure_ascii=False)

    def cargar_datos(self, libros_file="libros.json", usuarios_file="usuarios.json"):
        # Cargar libros
        if os.path.exists(libros_file):
            with open(libros_file, "r", encoding="utf-8") as f:
                libros_data = json.load(f)
                for libro_dict in libros_data:
                    libro = Libro.from_dict(libro_dict)
                    self.libros[libro.isbn] = libro
        # Cargar usuarios
        if os.path.exists(usuarios_file):
            with open(usuarios_file, "r", encoding="utf-8") as f:
                usuarios_data = json.load(f)
                for usuario_dict in usuarios_data:
                    usuario = Usuario.from_dict(usuario_dict, self.libros)
                    self.usuarios[usuario.id_usuario] = usuario


def menu():
    biblio = Biblioteca()
    biblio.cargar_datos()

    while True:
        print("\n--- Menú Biblioteca Digital ---")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros")
        print("8. Listar libros prestados a un usuario")
        print("9. Listar todos los libros disponibles")
        print("10. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblio.añadir_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a quitar: ")
            biblio.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID único del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblio.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("ID del usuario a dar de baja: ")
            biblio.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario: ")
            biblio.prestar_libro(isbn, id_usuario)

        elif opcion == "6":
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario: ")
            biblio.devolver_libro(isbn, id_usuario)

        elif opcion == "7":
            print("Buscar por: titulo, autor, categoria")
            criterio = input("Criterio: ").lower()
            if criterio not in ["titulo", "autor", "categoria"]:
                print("Criterio inválido.")
                continue
            valor = input("Valor a buscar: ")
            resultados = biblio.buscar_libros(criterio, valor)
            if resultados:
                print("Libros encontrados:")
                for libro in resultados:
                    print(libro)
            else:
                print("No se encontraron libros.")

        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            prestados = biblio.listar_prestados(id_usuario)
            if prestados:
                print(f"Libros prestados a {id_usuario}:")
                for libro in prestados:
                    print(libro)
            else:
                print("No hay libros prestados o usuario no registrado.")

        elif opcion == "9":
            biblio.listar_todos_los_libros()

        elif opcion == "10":
            print("Guardando datos y saliendo. ¡Hasta luego!")
            biblio.guardar_datos()
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()