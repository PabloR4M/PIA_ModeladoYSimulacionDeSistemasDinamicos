import math
from scipy.stats import chi2

RUTA_TABLA = r"../NumerosAleatoriosUniformes.txt"

def leer_tabla_txt(ruta):
    with open(ruta, 'r') as archivo:
        lineas = [line.strip() for line in archivo if line.strip()]
    tabla = []
    for i in range(0, len(lineas), 5):
        bloque = lineas[i:i+5]
        fila = []
        for linea in bloque:
            fila.append(linea.split(','))
        columnas = list(zip(*fila))
        tabla.append(columnas)
    return tabla

def prueba_series_desde_tabla():
    try:
        tabla = leer_tabla_txt(RUTA_TABLA)

        cantidad = int(input("¿Cuántos números rectangulares deseas tomar? "))
        columna = int(input("¿De qué columna (1-10)? ")) - 1
        fila_inicial = int(input("¿De qué fila inicial (1-8)? ")) - 1

        if not (0 <= columna < 10) or not (0 <= fila_inicial < len(tabla)):
            print("Columna o fila fuera de rango")
            return

        numeros = []
        fila_actual = fila_inicial
        while len(numeros) < cantidad and fila_actual < len(tabla):
            columna_datos = tabla[fila_actual][columna]
            for valor in columna_datos:
                if len(numeros) < cantidad:
                    numeros.append(int(valor) / 100000)
                else:
                    break
            fila_actual += 1

        if len(numeros) < cantidad:
            print(f"Solo se pudieron tomar {len(numeros)} números")
            return

        print("\nNúmeros rectangulares seleccionados:")
        for i, num in enumerate(numeros, start=1):
            print(f"  Número {i}: {num:.5f}")

        alpha_dato = float(input("\nIngresa el valor de alpha (en %): "))
        if not (0 < alpha_dato < 100):
            print("Alpha debe estar entre 0 y 100")
            return

        n_div = int(input("¿Cuántas divisiones por eje deseas usar (n)? "))
        if n_div <= 0:
            print("El número de divisiones debe ser mayor que cero")
            return

        # Paso 4: Generar pares (x, y)
        pares = [(numeros[i], numeros[i+1]) for i in range(cantidad - 1)]
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
        fei = (cantidad - 1) / (n_div ** 2)
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
        print(f"Xα^2 para α = {alpha_dato:.2f}% y gl = {grados_libertad}: {chi_critico:.5f}")

        # Paso 8: Comparación
        comparador = "<" if chi_cuadrado < chi_critico else ">"
        print(f"\nComparación: X0^2 = {chi_cuadrado:.5f} {comparador} Xα^2 = {chi_critico:.5f}")

        if chi_cuadrado < chi_critico:
            print("Los números son ACEPTADOS")
        else:
            print("Los números NO son aceptados")

        input("\nPresione ENTER para salir")

    except Exception as e:
        print(f"Error: {e}")

# Ejecutar la prueba
prueba_series_desde_tabla()