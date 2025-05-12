"""Juego de adivinanzas."""

import random

num_azar = random.randint(1, 100)
num_guess = 0
tries = 0


def juego_adivinanza(num):
    """Proporciona una pista al jugador."""
    if num_guess > num_azar:
        print("El número es mayor, vuelva a intentarlo")
    elif num_guess < num_azar:
        print("El número es menor, vuelva a intentarlo")


while True:
    num_guess = int(input("Ingrese un valor (1-100): "))
    if num_guess == num_azar:
        break

    juego_adivinanza(num_guess)
    tries += 1

print(f"Felicidades, adivinaste el número {num_guess} en {tries} intentos")
