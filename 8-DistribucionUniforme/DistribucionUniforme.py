
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
arreglo = []

for i in range(n):
    arreglo.append(float(input(f'Intoroduce el decimal #{i+1}')))

# 3. Mostrar resultado
print("\nArreglo generado (números entre 0 y 1):")
for numeros in arreglo:
    print(numeros)

# 4. Pedir a y b

a = float(input("Intoroduce la cantidad de a? "))
b = float(input("Intoroduce la cantidad de b? "))

#5. x_individual

x_individual = []

for numeros in arreglo:
    x_individual.append(a + (b - a) * numeros)

for numeros in x_individual:
    print(numeros)

# 6. total_de_x

total_de_x = 0

for numeros in x_individual:
    total_de_x += numeros

print("\nEl total de x es de: ", round(total_de_x, 5))

# 7. Promedio de x

promedio_de_x = total_de_x / n
print("\nEl promedio de x es de: ", round(promedio_de_x,5))