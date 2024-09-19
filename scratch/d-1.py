import math

# Números dados
n1 = 2154
n2 = 3110
n3 = 4066

# Cálculo de diferencias
d1 = n2 - n1
d2 = n3 - n2

# Encuentra el máximo común divisor entre d1 y d2
d = math.gcd(d1, d2)

# Calcula el residuo r al dividir los números entre d
r1 = n1 % d
r2 = n2 % d
r3 = n3 % d

# Verificar que los residuos son iguales
if r1 == r2 == r3:
    r = r1
else:
    raise ValueError("Los residuos no son iguales, lo cual es inesperado.")

# Calcula d - r
resultado = d - r

print(f"El valor de d - r es: {resultado}")
