import math
from scipy.stats import

def prueba_():
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

        # Paso 4: 

        # Paso n: Resultado final
        if z0 < z_tabla:
            print("\nLos números son ACEPTADOS")
        else:
            print("\nLos números NO son aceptados")

    except ValueError:
        print("Ingresa números validos")

# Ejecutar la prueba
prueba_()