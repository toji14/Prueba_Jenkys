"""devuelve un mensaje"""

# Aquí agregamos una línea en blanco (Línea 2)

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

# Aquí agregamos una línea en blanco (Línea 15)

if __name__ == "__main__":
    print(saludar("Usuario Jenkins"))
