#random viene instalada en la biblioteca estandar de python
import random
import msvcrt

caras_dado = 0

print("Cuantas caras tiene el dado?")
caras_dado = int(input())

while True:
    print("Pulsa cualquier tecla para lanzar el dado (Esc para salir)...")
    tecla = msvcrt.getch()
    if tecla == b'\x1b':  # Escape
        print("¡Has salido del programa!")
        break
    resultado = random.randint(1, caras_dado)
    print(f"Resultado: {resultado}")