import math
import random

def prueba_kolmogorov_automatica():
    try:
        # Paso 1: Solicitar cantidad de números
        n = int(input("¿Cuál es la cantidad de números rectangulares a generar? "))
        if n <= 0:
            print("La cantidad debe ser mayor que cero")
            return

        # Paso 2: Generar números rectangulares automáticamente
        numeros = [round(random.random(), 5) for _ in range(n)]
        print("\nNúmeros rectangulares generados:")
        for i, num in enumerate(numeros, start=1):
            print(f"  Número {i}: {num}")

        # Paso 3: Solicitar valor de alpha en %
        alpha_dato = float(input("\nIngresa el valor de alpha (en %): "))
        if not (0 < alpha_dato < 100):
            print("Alpha debe estar entre 0 y 100")
            return

        # Paso 4:Generar tabla de comparación
        numeros_ordenados = sorted(numeros)
        print("\ni   |    xi    |  F(xi) = i/N  |  |F(xi) - xi|")
        print("-" * 42)

        diferencias = []
        for i, xi in enumerate(numeros_ordenados, start=1):
            fxi = i / n
            diferencia = abs(fxi - xi)
            diferencias.append(diferencia)
            print(f"{i:3d} | {xi:8.5f} | {fxi:13.5f} | {diferencia:13.5f}")

        # Paso 5: Calcular DA
        da_max = max(diferencias)
        print(f"\nDA = {da_max:.5f}")

        # Paso 6: Calcular Zalpha,N
        alpha_decimal = alpha_dato / 100
        zalpha_n = round(math.sqrt(-0.5 * math.log(alpha_decimal / 2)) / math.sqrt(n), 5)
        print(f"Zα,N para α = {alpha_dato:.2f}% y N = {n}: {zalpha_n:.5f}")

        # Paso 7: Comparación final
        comparador = "<" if da_max < zalpha_n else ">"
        print(f"\nComparación: DA = {da_max:.5f} {comparador} Zα,N = {zalpha_n:.5f}")

        if da_max < zalpha_n:
            print("Los números son ACEPTADOS")
        else:
            print("Los números NO son aceptados")

    except ValueError:
        print("Ingresa valores válidos")

# Ejecutar la prueba
prueba_kolmogorov_automatica()