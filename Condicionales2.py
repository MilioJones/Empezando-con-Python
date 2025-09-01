print("Escribe tu nombre:")
nombre = input()
print("Escribe tu edad:")
edad = int(input())

#elif
#Operadores lógicos

if nombre == "Emilio" and edad > 18:
    print("Saludos Emilio, eres mayor de edad")
elif nombre == "Emilio" and edad < 18:
    print("Saludos Emilio, eres menor de edad")
else:
    print(f"Saludos {nombre}, no eres Emilio")
