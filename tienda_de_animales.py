print("************************************")
print(" Bienvenido a la tienda de animales")
print("************************************")

num_perros = 10
num_gatos = 8
num_pajaros = 25

animales_totales = num_perros + num_gatos + num_pajaros

print("Ingresa tu nombre:")
nombre = input()
print("Ingresa tu apellido:")
apellido = input()

#concatenacion
nombre_completo = nombre + " " + apellido

print(f"Gracias por visitarnos {nombre_completo}")

print("Selecciona la opción que deseas:")
print("1. Ver animales disponibles")
print("2. Adoptar un animal")
print("3. Salir")
respuesta = int(input())

while respuesta == 1 or respuesta == 2:
    if respuesta == 1:
        print("Actualmente contamos con:")
        print(f"{num_perros} perros, {num_gatos} gatos y {num_pajaros} pájaros")
        print(f"En total tenemos {animales_totales} animales disponibles para la adopción")
    elif respuesta == 2:
        print("¿Qué tipo de animal deseas adoptar?")
        print("1. Perro")
        print("2. Gato")
        print("3. Pájaro")
        tipo_animal = int(input())
        
        if tipo_animal == 1:
            if num_perros > 0:
                num_perros -= 1
                print(f"Felicidades {nombre}, has adoptado un perro!")
                print(" ")
            else:
                print("Lo siento, no tenemos perros disponibles para adopción.")
        elif tipo_animal == 2:
            if num_gatos > 0:
                num_gatos -= 1
                print(f"Felicidades {nombre}, has adoptado un gato!")
                print(" ")
            else:
                print("Lo siento, no tenemos gatos disponibles para adopción.")
        elif tipo_animal == 3:
            if num_pajaros > 0:
                num_pajaros -= 1
                print(f"Felicidades {nombre}, has adoptado un pájaro!")
                print(" ")
            else:
                print("Lo siento, no tenemos pájaros disponibles para adopción.")
                 
    print("Selecciona la opción que deseas:")
    print("1. Ver animales disponibles")
    print("2. Adoptar un animal")
    print("3. Salir")
    respuesta = int(input())
if respuesta == 3:
    print(f"Gracias por visitarnos {nombre}, vuelve pronto!")
else:
    print("Opción no válida.")

print(" ")
print("************************************")
print(f"Animales restantes: {num_perros} perros, {num_gatos} gatos, {num_pajaros} pájaros")
print("************************************")

