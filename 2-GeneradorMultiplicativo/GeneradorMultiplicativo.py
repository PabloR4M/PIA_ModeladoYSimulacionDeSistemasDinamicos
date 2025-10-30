import math

def lcg_multiplicativo(a, m, x0):
    x = x0
    valores_generados = set()
    ciclo_detectado = False

    print(f"{'i':>3} | x0 |{'(a*Xn) mod m' :>20}")
    print("-" * 50)

    for i in range(1, m + 1):
        raw = a * x
        decimal, entera = math.modf(raw / m)
        modulo = int(decimal * m + 0.1)

        print(f"{i:3d} | {x:3d} | {int(entera)} + {modulo}/{m} | {modulo:3d} | {modulo}/{m} = {decimal:6f}")

        if modulo in valores_generados:
            print(f"\nCICLO DETECTADO\nGENERADOR CONGRUENCIAL MULTIPLICATIVO NO CONFIABLE")
            ciclo_detectado = True
            break

        valores_generados.add(modulo)
        x = raw % m

    if not ciclo_detectado:
        print("\nGENERADOR CONGRUENCIAL MULTIPLICATIVO " + ("CONFIABLE" if x == x0 else "NO CONFIABLE"))

# Solicitar parámetros al usuario
try:
    a = int(input("Introduce el valor de a: "))
    m = int(input("Introduce el valor de m: "))
    x0 = int(input("Introduce el valor de X0: "))
    if m <= 1:
        print("El valor de m debe ser mayor que 1 para evitar división por cero.")
    else:
        lcg_multiplicativo(a, m, x0)
except ValueError:
    print("Introduce solo números enteros.")