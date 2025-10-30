import math

def lcg(a, c, m, x0):
    x = x0
    valores_generados = set()
    ciclo_detectado = False

    print(f"{'i':>3} | x0 |{'(a*Xn+C) mod m' :>20}")
    print("-" * 50)

    for i in range(1, m+1):
        raw = a * x + c
        decimal, entera = math.modf(raw / m)
        modulo = int(decimal * m + 0.1)

        print(f"{i:3d} | {x:3d} | {int(entera)} + {modulo}/{m} | {modulo:3d} | {modulo}/{m} = {decimal:6f}")

        if modulo in valores_generados:
            print(f"\nCICLO DETECTADO \nGENERADOR CONGRUENCIAL MIXTO NO CONFIABLE")
            ciclo_detectado = True
            break

        valores_generados.add(modulo)
        x = raw % m

    if not ciclo_detectado:
        print("\nGENERADOR CONGRUENCIAL MIXTO " + ("CONFIABLE" if x == x0 else "NO CONFIABLE"))

    input("\nPresione ENTER para salir")

a, x0, c, m = 5,4,7,8
lcg(a, c, m, x0)