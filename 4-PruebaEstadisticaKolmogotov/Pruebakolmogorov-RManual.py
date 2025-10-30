import math

def prueba_kolmogorov():
    try:
        # Paso 1: Solicitar cantidad de números
        n = int(input("¿Cuántos números rectangulares vas a ingresar? "))
        if n <= 0:
            print("La cantidad debe ser mayor que cero")
            return

        # Paso 2: Ingresar los números
        numeros = []
        print("Ingresa los números rectangulares (valores entre 0 y 1):")
        for i in range(n):
            x = float(input(f"  Número {i+1}: "))
            if not (0 <= x <= 1):
                print("  El número debe estar entre 0 y 1")
                return
            numeros.append(x)

        # Paso 3: Solicitar valor de alpha en %
        alpha_dato = float(input("Ingresa el valor de alpha (en %): "))
        if not (0 < alpha_dato < 100):
            print("Alpha debe estar entre 0 y 100")
            return

        # Paso 4: Generar tabla de comparación
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
        print("Ingresa números válidos")

# Ejecutar la prueba
prueba_kolmogorov()