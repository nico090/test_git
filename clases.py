class Persona:
    def __init__(self, nombre: str, edad: int, dni: int, sexo: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.sexo = sexo


# Crear una instancia de la clase
fare = Persona(nombre="fare", edad=26, dni=41718263871, sexo="m")

# Imprimir la instancia
print(fare.__dict__)
