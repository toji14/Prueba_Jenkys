"""devuelve un mensaje"""

def saludar(nombre):
    """
    Devuelve un saludo.

    Si se proporciona un nombre, saluda a la persona.
    Si no se proporciona un nombre (o es None/vacío), saluda al mundo.
    """
    if nombre:
        return f"Hola, {nombre}!"
    else:
        return "Hola, Mundo!"

# Esto permite ejecutar la función si corres el archivo directamente
if __name__ == "__main__":
    print(saludar("Usuario Jenkins"))
