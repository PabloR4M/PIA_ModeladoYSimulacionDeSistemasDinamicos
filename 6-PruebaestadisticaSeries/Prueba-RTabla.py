import math
from scipy.stats import 

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

def prueba__desde_tabla():
    try:
        tabla = leer_tabla_txt(RUTA_TABLA)

        # Paso 1: Solicitar cantidad, columna y fila
        cantidad = int(input("¿Cuántos números rectangulares deseas tomar? "))
        columna = int(input("¿De qué columna (1-10)? ")) - 1
        fila_inicial = int(input("¿De qué fila inicial (1-8)? ")) - 1

        if not (0 <= columna < 10) or not (0 <= fila_inicial < len(tabla)):
            print("Columna o fila fuera de rango.")
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

        # Paso 3: Solicitar alpha
        alpha_dato = float(input("\nIngresa el valor de alpha (en %): "))
        if not (0 < alpha_dato < 100):
            print("Alpha debe estar entre 0 y 100")
            return

        # Paso 4: 

        # Paso n: Resultado
        if z0 < z_tabla:
            print("\nLos números son ACEPTADOS")
        else:
            print("\nLos números NO son aceptados")

    except Exception as e:
        print(f"Error: {e}")

# Ejecutar la prueba
prueba__desde_tabla()