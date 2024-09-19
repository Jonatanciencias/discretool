import math

a = 123456789
b = 987654321
c = 135792468

d1 = abs(a - b)
d2 = abs(b - c)

d = math.gcd(d1, d2)
print(f"El mcd comun es: {d}")
print(f"{d1} dividido entre {d} es: q:{d1 / d}, r:{d1 % d}")
print(f"{d2} dividido entre {d} es: q:{d2 / d}, r:{d2 % d}")
