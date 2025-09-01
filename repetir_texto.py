print("Ingresa un texto cualquiera:")
texto = input()
print("El texto que has introducido es el siguiente:")
print(texto)
print("¿Cuantas veces quieres que se repita el texto?")
num_repeticiones = int(input())
for i in range(num_repeticiones):
    print(texto)