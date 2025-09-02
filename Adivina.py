import random

def tirar_dados():
    return random.randint(2, 12)

def pedir_respuesta():
    print(" ")
    print("Ingresa tu predicción")
    print("1. Impar")
    print("2. Par")
    print("3. Salir")
    respuesta = int(input("Tu elección: "))
    return respuesta

def imprimir_resultado(prediccion, numero):
    if (numero % 2 == 0 and prediccion == 2) or (numero % 2 != 0 and prediccion == 1):
        print(" ")
        print(f"¡Correcto! El número fue {numero}.")
    else:
        print(" ")
        print(f"Incorrecto. El número fue {numero}.")

while True:
        numero = tirar_dados()
        prediccion = pedir_respuesta()
        if prediccion == 3:
            break
        imprimir_resultado(prediccion, numero)

print(" ")
print("Gracias por jugar")