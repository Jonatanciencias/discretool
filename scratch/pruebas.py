import math

def calcular_mcd_mcm(a: int, b: int):
    mcd = math.gcd(a, b)
    
    mcm = abs(a * b) // mcd
    
    return mcd, mcm

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

mcd, mcm = calcular_mcd_mcm(numero1, numero2)

print(f"El Máximo Común Divisor de {numero1} y {numero2} es: {mcd}")
print(f"El Mínimo Común Múltiplo de {numero1} y {numero2} es: {mcm}")