import random
import math

# 1. Pedir la cantidad de números
while True:
    try:
        n = int(input("¿Cúal es la cantidad de R? "))
        if n <= 0:
            print("Debe ser un número entero positivo.")
            continue
        break
    except ValueError:
        print("Error: ingresa un número entero válido.")



# 2. Generar los números (entre 0 y 1)
arreglo = [round(random.random(), 5) for _ in range(n)]

# 3. Mostrar resultado
print("\nArreglo generado (números entre 0 y 1):")
for numeros in arreglo:
    print(numeros)

#4. Pedir lambda

a = input('\nIntroduce lambda:')

# 5. Obtener x individual
x_individual = []

for numeros in arreglo:
    x = (-1 / int(a)) * math.log(numeros)
    x_individual.append(round(x, 5))

for numeros in x_individual:
    print(numeros)

#6. Obtener total de x_individual

total_de_x = 0

for numeros in x_individual:
    total_de_x += numeros

print(f'\ntotal_de_x = {total_de_x}')

#7. Promedio de total_de_x

promedio_de_x = total_de_x / len(x_individual)
print(f'\npromedio_de_x = {promedio_de_x}')
