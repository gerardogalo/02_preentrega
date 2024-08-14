from .base_datos import socios


class Administracion:
    def __init__(self) -> None:
        self.socios = socios
        # tipo self.nombre = name

    def __str__(self):
        return "Instancia de Administracion."  # Aca podes ponerle un nombre
        # return f"Administracion: {self.nombre}"

        # if not self.socios:
        #     return "No hay socios registrados actualmente"
        # total_socios = len(self.socios)
        # activos = sum(1 for socio in self.socios if socio['activo'])
        # return f"Total de socios registrados: {total_socios}, Socios activos: {activos}"

    def validar_usuario(self, usuario: str) -> bool:
        """Valida el nombre de usuario según el criterio: solo letras y entre 4 y 11 caracteres."""
        if not usuario.isalpha() or not (3 < len(usuario) < 12):
            print(
                "El usuario debe contener solo letras y tener entre 4 y 11 caracteres. Intente nuevamente"
            )
            return False
        return True

    def validar_contraseña(self, contraseña: str) -> bool:
        """Valida la contraseña según el criterio: solo números y entre 5 y 8 dígitos."""
        if not contraseña.isdigit() or not (4 < len(contraseña) < 9):
            print(
                "La contraseña debe ser numérica y tener entre 5 y 8 dígitos. Intente nuevamente"
            )
            return False
        return True

    def pedir_usuario(self) -> str:
        """Solicita al usuario ingresar un nombre de usuario válido que no esté registrado."""
        while True:
            usuario = input("Ingrese el nombre de usuario: ").lower()
            if usuario in [socio["nombre"] for socio in self.socios]:
                print("🚨 Este usuario ya está registrado. Intente con otro nombre.")
                continue
            if self.validar_usuario(usuario):
                return usuario

    def pedir_contraseña(self) -> str:
        """Solicita al usuario ingresar una contraseña válida."""
        while True:
            contraseña = input("Ingrese la contraseña del asociado: ")
            if self.validar_contraseña(contraseña):
                return contraseña

    def registrar_socio(self):
        """Registra un nuevo socio si el nombre de usuario es válido y no está duplicado."""
        usuario = self.pedir_usuario()
        contraseña = self.pedir_contraseña()
        email = input("Ingrese el email del socio: ")
        edad = int(input("Ingrese la edad del socio: "))
        self.socios.append(
            {
                "nombre": usuario,
                "contraseña": contraseña,
                "email": email,
                "activo": True,
                "edad": edad,
            }
        )
        print(f"✔️ El socio {usuario} ha sido registrado correctamente.")

    def publica_socios(self):
        """Imprime todos los socios registrados nombre, correo y estado"""
        if not self.socios:
            print("🚨 No hay socios registrados aún.")
            return
        print("\nListado de socios registrados:")
        for socio in self.socios:
            estado = "Activo" if socio["activo"] else "Inactivo"
            print(
                f"Socio: {socio['nombre']}, Estado: {estado}, Email: {socio['email']}"
            )

    def acceso_socios(self):
        """Permite el acceso a los socios verificando usuario y contraseña"""
        usuario = input("Ingrese el nombre del socio: ").lower()
        contraseña = input("Ingrese la contraseña: ")
        for socio in self.socios:
            if socio["nombre"] == usuario and socio["contraseña"] == contraseña:
                print(f"✔️ Bienvenido {usuario} 👋")
                return
        print("❌ La contraseña no coincide o el usuario no existe.")

    def elimina_socio(self):
        """Elimina un socio del registro si el nombre de usuario existe."""
        usuario = input("Ingrese el nombre del socio a eliminar: ").lower()
        contraseña = input("Ingrese la contraseña del socio a eliminar: ")
        for socio in self.socios:
            if socio["nombre"] == usuario and socio["contraseña"] == contraseña:
                self.socios.remove(socio)
                print(f"✔️ El socio {usuario} ha sido eliminado correctamente.")
                return
        print("🚨 Usuario no encontrado o contraseña incorrecta.")
