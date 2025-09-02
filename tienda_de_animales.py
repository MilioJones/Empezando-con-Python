print("************************************")
print(" Bienvenido a la tienda de animales")
print("************************************")

num_perros = 10
num_gatos = 8
num_pajaros = 25
nombre = ""
apellido = ""
respuesta = 1
perros_adoptados = 0
gatos_adoptados = 0
pajaros_adoptados = 0

animales_totales = num_perros + num_gatos + num_pajaros

def menu():
    print(" ")
    print("1. Ver animales disponibles")
    print("2. Adoptar un animal")
    print("3. Salir")
    opcion1=int(input("Opción: "))
    return (opcion1)

def ver_animales():
    print("Actualmente contamos con:")
    print(" ")
    print(f"{num_perros} perros, {num_gatos} gatos y {num_pajaros} pájaros")
    print(f"En total tenemos {animales_totales} animales disponibles para la adopción")

def adopcion():
    print("¿Qué tipo de animal deseas adoptar?")
    print("1. Perro")
    print("2. Gato")
    print("3. Pájaro")
    opcion2 = int(input("Opción: "))
    return (opcion2)

while nombre == "":
    print("Ingresa tu nombre:")
    nombre = input()
while apellido == "":
    print("Ingresa tu apellido:")
    apellido = input()

#concatenacion
nombre_completo = nombre + " " + apellido

print(" ")
print(f"Gracias por visitarnos {nombre_completo}")


while respuesta == 1 or respuesta == 2:
    respuesta=menu()
    
    if respuesta == 1:
        ver_animales()
        print(" ")
    elif respuesta == 2:
        tipo_animal = adopcion()
        print(" ")
        if tipo_animal == 1:
            if num_perros > 0:
                num_perros -= 1
                perros_adoptados += 1
                print(f"Felicidades {nombre}, has adoptado un perro!")
                print(" ")
            else:
                print("Lo siento, no tenemos perros disponibles para adopción.")
        elif tipo_animal == 2:
            if num_gatos > 0:
                num_gatos -= 1
                gatos_adoptados += 1
                print(f"Felicidades {nombre}, has adoptado un gato!")
                print(" ")
            else:
                print("Lo siento, no tenemos gatos disponibles para adopción.")
        elif tipo_animal == 3:
            if num_pajaros > 0:
                num_pajaros -= 1
                pajaros_adoptados += 1
                print(f"Felicidades {nombre}, has adoptado un pájaro!")
                print(" ")
            else:
                print("Lo siento, no tenemos pájaros disponibles para adopción.")
                 
    elif respuesta == 3:
        print(f"Gracias por visitarnos {nombre}, vuelve pronto!")
        print(" ")
        print(f"Has adoptado {perros_adoptados} perros, {gatos_adoptados} gatos y {pajaros_adoptados} pájaros")
    else:
        print("Opción no válida.")

print(" ")
print("************************************")
print(f"Animales restantes: {num_perros} perros, {num_gatos} gatos, {num_pajaros} pájaros")
print("************************************")

