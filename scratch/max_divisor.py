import math

# Datos de entrada
a = 123456789
b = 987654321
c = 135792468

# Cálculo de diferencias
d1 = a - b
d2 = b - c

# Encuentra el máximo común divisor entre d1 y d2
d = math.gcd(d1, d2)

print(f"El mayor número entero d que divide a (a-b) y (b-c) es: {d}")
