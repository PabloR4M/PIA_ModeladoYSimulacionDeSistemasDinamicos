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
arreglo = []

for i in range(n):
    arreglo.append(float(input(f'Intoroduce el decimal #{i+1}: ')))

# 3. Mostrar resultado
print("\nR:")
for numeros in arreglo:
    print(numeros)

# 4. Generar tabla

num_terminos = 500  # número máximo de términos a calcular

fi = []
Fi = []

print(f"x | f(xi)     | F(xi)")

for x in range(num_terminos):
    f = (math.exp(-n) * (n ** x)) / math.factorial(x)
    fi.append(round(f, 5))

    # frecuencia acumulada
    if not Fi:
        Fi.append(f)
    else:
        Fi.append(Fi[-1] + f)

    # imprimir
    print(f"{x} | {f:.5f} | {Fi[-1]:.5f}")

    # detener si la acumulada llega a 1
    if Fi[-1] >= 0.9999:
        break

# 5. Asignar valor a cada termino de R

valor = 0
longitud = len(arreglo)

for j in range(longitud):
    r = arreglo[j]
    for i in range(len(Fi)):
        if i == 0:
            a = 0
            b = Fi[i]
        else:
            a = Fi[i]
            b = Fi[i + 1]

        if a < r <= b:
            valor += i + 1
            break

print("Valor acumulado:", valor)