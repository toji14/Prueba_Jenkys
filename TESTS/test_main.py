"""Importa la función que quieres probar desde el archivo main.py"""

# Asegúrate que la ruta de importación sea correcta según la estructura de tu proyecto
from APP.main import saludar

def test_saludar_con_nombre():
    """Prueba que la función salude correctamente con un nombre."""
    assert saludar("Alice") == "Hola, Alice!"

def test_saludar_sin_nombre():
    """Prueba que la función salude al mundo si no se da nombre (cadena vacía)."""
    assert saludar("") == "Hola, Mundo!"

def test_saludar_none():
    """Prueba que la función salude al mundo si no se da nombre (valor None)."""
    assert saludar(None) == "Hola, Mundo!"

def test_saludar_otro_nombre():
    """Otra prueba con un nombre diferente."""
    assert saludar("Bob") == "Hola, Bob!"
