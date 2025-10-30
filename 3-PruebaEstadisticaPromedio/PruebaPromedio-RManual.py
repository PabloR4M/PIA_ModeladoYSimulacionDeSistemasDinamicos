import math
from scipy.stats import norm

def prueba_promedio():
    try:
        # Paso 1: Solicitar cantidad de números
        n = int(input("¿Cuántos números rectangulares vas a ingresar? "))
        if n <= 0:
            print("La cantidad debe ser mayor que cero.")
            return

        # Paso 2: Ingresar los números
        numeros = []
        print("Ingresa los números rectangulares (valores entre 0 y 1):")
        for i in range(n):
            x = float(input(f"  Número {i+1}: "))
            if not (0 <= x <= 1):
                print("  El número debe estar entre 0 y 1.")
                return
            numeros.append(x)

        # Paso 3: Solicitar valor de alpha en %
        alpha_dato = float(input("Ingresa el valor de alpha (en %): "))
        if not (0 < alpha_dato < 100):
            print("Alpha debe estar entre 0 y 100.")
            return

        # Paso 4: Calcular sumatoria y promedio
        suma = sum(numeros)
        promedio = suma / n
        print(f"\nSumatoria de X: {suma:.6f}")
        print(f"Promedio de X: {promedio:.6f}")

        # Paso 5: Calcular Z0
        z0 = abs((promedio - 0.5) * math.sqrt(n) / math.sqrt(1/12))
        print(f"\nZ0 calculado: {z0:.6f}")

        # Paso 6: Calcular Zα/2 usando alpha_dato
        alpha_decimal = alpha_dato / 100
        z_tabla = norm.ppf(1 - alpha_decimal / 2)
        print(f"Zα/2 para α = {alpha_dato:.2f}%: {z_tabla:.2f}")

        # Paso 7: Mostrar comparación
        comparador = "<" if z0 < z_tabla else ">"
        print(f"\nComparación: Z0 = {z0:.6f} {comparador} Zα/2 = {z_tabla:.2f}")

        # Paso 8: Resultado final
        if z0 < z_tabla:
            print("\nLos números son ACEPTADOS")
        else:
            print("\nLos números NO son aceptados")

    except ValueError:
        print("Ingresa números validos")

# Ejecutar la prueba
prueba_promedio()