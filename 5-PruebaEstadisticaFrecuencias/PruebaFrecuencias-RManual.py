import math
from scipy.stats import chi2

def prueba_frecuencias():
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
        fei = n / n_intervalos
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

    except Exception as e:
        print(f"Error: {e}")

# Ejecutar la prueba
prueba_frecuencias()