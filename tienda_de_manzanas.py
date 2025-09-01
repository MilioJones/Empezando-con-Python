num_manzanas = 20 #Definimos la cantidad de manzanas disponibles
precio_manzanas = 5 #Definimos el precio por manzana

print("Bienvenido a la tienda de manzanas") #Damos la bienvenida al usuario

print("¿Como te llamas?") #Preguntamos el nombre del usuario
nombre = input() #Guardamos el nombre del usuario en una variable

print(f"Hola {nombre}, actualmente tenemos {num_manzanas} manzanas disponibles a un precio de {precio_manzanas}€ cada una.") #Mostramos la cantidad de manzanas y el precio al usuario
print("¿Cuántas manzanas quieres comprar?") #Preguntamos cuántas manzanas quiere comprar el usuario
num_comprar = int(input()) #Guardamos la cantidad de manzanas que quiere comprar en una variable
if num_comprar >  num_manzanas: #Si la cantidad que quiere comprar es mayor que la cantidad disponible
    print(f"Lo siento {nombre}, no tenemos suficientes manzanas para tu compra.") #Mostramos un mensaje de error    
else: #Si la cantidad que quiere comprar es menor o igual que la cantidad disponible
    total = num_comprar * precio_manzanas #Calculamos el total a pagar
    print(f"{nombre} has comprado {num_manzanas}.")
    print(f"El total a pagar es de {total}€.")
    print("Gracias por tu compra. Vuelve pronto!") #Agradecemos la compra al usuario
    print(" ")
    num_manzanas = num_manzanas - num_comprar
    print(f"Ahora quedan {num_manzanas} manzanas en stock.")
