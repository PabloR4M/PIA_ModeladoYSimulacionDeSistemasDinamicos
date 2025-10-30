import math
import random
from scipy.stats import 

def prueba__automatica():
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

        # Paso 4: 

        # Paso n: Resultado final
        if z0 < z_tabla:
            print("\nLos números son ACEPTADOS")
        else:
            print("\nLos números NO son aceptados")

    except ValueError:
        print("Ingresa valores válidos")

# Ejecutar la prueba
prueba__automatica()