import math
import random
from scipy.stats import chi2

def prueba_series_automatica():
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

        n_div = int(input("¿Cuántas divisiones por eje deseas usar (n)? "))
        if n_div <= 0:
            print("El número de divisiones debe ser mayor que cero")
            return

        # Paso 4: Generar pares (x, y)
        pares = [(numeros[i], numeros[i+1]) for i in range(n - 1)]
        rango = 1 / n_div
        frecuencias = [[0 for _ in range(n_div)] for _ in range(n_div)]

        print("\nTabla de pares (X, Y) y cuadrante:")
        print(f"{'X':>8} {'Y':>8} {'Cuadrante':>10}")
        print("-" * 30)
        for i in range(len(numeros) - 1):
            x = numeros[i]
            y = numeros[i + 1]
            j = min(int(x / rango), n_div - 1)
            k = min(int(y / rango), n_div - 1)
            frecuencias[k][j] += 1
            cuadrante = f"{chr(65 + k)}{j + 1}"
            print(f"{x:8.5f} {y:8.5f} {cuadrante:>10}")

        # Imprimir última X sin Y ni cuadrante
        ultima_x = numeros[-1]
        print(f"{ultima_x:8.5f} {'':>8} {'':>10}")

        # Paso 5: Imprimir cuadrantes de abajo hacia arriba
        print("\nFrecuencia por cuadrante (orientación inferior izquierda = 0):")
        encabezado = "     " + "  ".join([f"{j+1:>4}" for j in range(n_div)])
        print(encabezado)
        print("    " + "-" * (5 * n_div))
        for i in reversed(range(n_div)):
            fila = "  ".join(f"{frecuencias[i][j]:4d}" for j in range(n_div))
            print(f"{chr(65 + i)} | {fila}")

        # Paso 6: Calcular X0^2
        fei = (n - 1) / (n_div ** 2)
        chi_cuadrado = 0
        for i in range(n_div):
            for j in range(n_div):
                foi = frecuencias[i][j]
                chi_cuadrado += ((foi - fei) ** 2) / fei

        print(f"\nX0^2 = {chi_cuadrado:.5f}")

        # Paso 7: Valor crítico
        alpha_decimal = alpha_dato / 100
        grados_libertad = n_div ** 2 - 1
        chi_critico = round(chi2.ppf(1 - alpha_decimal, grados_libertad), 5)
        print(f"Xα^2 para α = {alpha_dato:.2f}% y n = {grados_libertad}: {chi_critico:.5f}")

        # Paso 8: Comparación
        comparador = "<" if chi_cuadrado < chi_critico else ">"
        print(f"\nComparación: X0^2 = {chi_cuadrado:.5f} {comparador} Xα^2 = {chi_critico:.5f}")

        if chi_cuadrado < chi_critico:
            print("Los números son ACEPTADOS")
        else:
            print("Los números NO son aceptados")

    except Exception as e:
        print(f"Error: {e}")

# Ejecutar la prueba
prueba_series_automatica()