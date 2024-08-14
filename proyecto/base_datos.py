socios = [
    {
        "nombre": "juancito",
        "contraseña": "123456",
        "email": "juan@mail.com",
        "activo": True,
        "edad": 28,
    },
    {
        "nombre": "messi",
        "contraseña": "101010",
        "email": "messi@mail.com",
        "activo": True,
        "edad": 35,
    },
    {
        "nombre": "lionel",
        "contraseña": "111111",
        "email": "lionel@mail.com",
        "activo": True,
        "edad": 22,
    },
    {
        "nombre": "andres",
        "contraseña": "987654",
        "email": "andres@mail.com",
        "activo": False,
        "edad": 18,
    },
]


"""
Me refiero a que utilices esto >

socios = {
    "juancito": {
        "password": "123456",
        "email": "juan@mail.com",
        "activo": True,
        "edad": 35
    },
    ....
    Y asi vas agregando registros de socios. Esto es mucho mas rapido y eficiente
}

Lo de crear socios seria cuando registres un nuevo socio, instancies una clase Socio (tendrias que crearla) y te quedaria asi la estructura >

socios = {
    "juancito": Socio,
    "maria": Socio,
    "Nico": Socio,
}

Cada instancia de Socio, guarda toda la info de antes, podras controlar mejor la informacion asi y tenerla mas encapsulada. Podemos modelar metodos
para obtener la info.
"""
