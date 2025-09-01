print("Introduce un numero del 1 al 100")
num = int(input())
if num < 1:
    print("Por favor introduce un numero mayor a 0")
elif num > 100:
    print("Por favor introduce un numero menor a 100")
else:
    print(f"Muy bien! el {num} es una gran opción")