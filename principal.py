"""
Objetivo: Practicar el concepto de Clases y Objetos.
Crear un programa que permita el modelamiento de socios/usuarios en una página web ficticia. Se debe utilizar el concepto de Programación Orientada a Objetos.
Se evaluará el uso correcto de atributos y métodos:
Crea un paquete que contenga dos módulos:
-El primer módulo debe contener a la clase Socios: debe tener mínimo 4 atributos y 2 métodos.
-El segundo módulo debe crear instancias de Socios
Se debe utilizar el método y si es posible usar herencia
REVISAR MEJORAS
"""

from proyecto.administracion import Administracion


def menu(admin):
    while True:
        print(
            "\n1. Registrar Socio\n2. Publicar Socios\n3. Acceso de Socios\n4. Eliminar Socio\n5. Salir"
        )
        opción = input("Seleccione una opción: ")
        if opción == "1":
            admin.registrar_socio()
        elif opción == "2":
            admin.publica_socios()
        elif opción == "3":
            admin.acceso_socios()
        elif opción == "4":
            admin.elimina_socio()
        elif opción == "5":
            print("Gracias por usar nuestro sistema. ¡Hasta la próxima! 😊")
            break
        else:
            print("Opción no válida, intente de nuevo.")


def main():
    admin = Administracion()  # Aca podes pasarle el nombre, como Socios SA
    print(admin)  # Muestra una descripción simple de la instancia
    menu(admin)


if __name__ == "__main__":
    main()
