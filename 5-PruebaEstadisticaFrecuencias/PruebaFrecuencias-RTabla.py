import math
from scipy.stats import chi2

# Ruta fija del archivo
RUTA_TABLA = r"../NumerosAleatoriosUniformes.txt"

def leer_tabla_txt(ruta):
    with open(ruta, 'r') as archivo:
        lineas = [line.strip() for line in archivo if line.strip()]
    tabla = []

    # Agrupar cada 5 líneas como una fila
    for i in range(0, len(lineas), 5):
        bloque = lineas[i:i+5]
        fila = []
        for linea in bloque:
            fila.append(linea.split(','))
        columnas = list(zip(*fila))  # Transponer para obtener columnas
        tabla.append(columnas)
    return tabla  # tabla[fila][columna][renglón]

def prueba_frecuencias_desde_tabla():
    try:
        tabla = leer_tabla_txt(RUTA_TABLA)

        # Paso 1: Solicitar cantidad, columna y fila
        cantidad = int(input("¿Cuántos números rectangulares deseas tomar? "))
        columna = int(input("¿De qué columna (1-10)? ")) - 1
        fila_inicial = int(input("¿De qué fila inicial (1-8)? ")) - 1

        if not (0 <= columna < 10) or not (0 <= fila_inicial < len(tabla)):
            print("Columna o fila fuera de rango")
            return

        # Paso 2: Extraer los números recorriendo filas
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
            print(f"Solo se pudieron tomar {len(numeros)} números. No hay suficientes datos en esa columna")
            return

        print("\nNúmeros rectangulares seleccionados:")
        for i, num in enumerate(numeros, start=1):
            print(f"  Número {i}: {num:.5f}")

        # Paso 3: Solicitar alpha y número de intervalos n
        alpha_dato = float(input("\nIngresa el valor de alpha (en %): "))
        if not (0 < alpha_dato < 100):
            print("Alpha debe estar entre 0 y 100")
            return

        n_intervalos = int(input("¿Cuántos intervalos deseas usar (n)? "))
        if n_intervalos <= 0:
            print("El número de intervalos debe ser mayor que cero")
            return

        # Paso 4: Generar tabla de frecuencias
        fei = cantidad / n_intervalos
        rango = 1 / n_intervalos
        etiquetas = [chr(65 + i) for i in range(n_intervalos)]
        frecuencias = [0] * n_intervalos

        for num in numeros:
            indice = min(int(num / rango), n_intervalos - 1)
            frecuencias[indice] += 1

        print("\n     |  FEi  |  FOi")
        print("-" * 22)
        for i in range(n_intervalos):
            print(f"  {etiquetas[i]}  | {fei:6.2f} | {frecuencias[i]:4d}")

        # Paso 5: Calcular X0^2
        chi_cuadrado = sum(((foi - fei) ** 2) / fei for foi in frecuencias)
        print(f"\nX0^2 = {chi_cuadrado:.5f}")

        # Paso 6: Calcular valor crítico chi^2
        alpha_decimal = alpha_dato / 100
        grados_libertad = n_intervalos - 1
        chi_critico = round(chi2.ppf(1 - alpha_decimal, grados_libertad), 5)
        print(f"Xα^2 para α = {alpha_dato:.2f}% y n = {grados_libertad}: {chi_critico:.2f}")

        # Paso 7: Comparación final
        comparador = "<" if chi_cuadrado < chi_critico else ">"
        print(f"\nComparación: X0^2 = {chi_cuadrado:.5f} {comparador} Xα^2 = {chi_critico:.2f}")

        if chi_cuadrado < chi_critico:
            print("Los números son ACEPTADOS")
        else:
            print("Los números NO son aceptados")

        input("\nPresione ENTER para salir")

    except Exception as e:
        print(f"Error: {e}")

# Ejecutar la prueba
prueba_frecuencias_desde_tabla()