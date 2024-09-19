'''
Encuentre el menor entero positivo n tal que 15\mid (n+4) y 23\mid(n+2)
'''

class ChineseRemainderTheorem:
    def __init__(self, a1, m1, a2, m2):
        self.a1 = a1  # Residuo de la primera congruencia
        self.m1 = m1  # Módulo de la primera congruencia
        self.a2 = a2  # Residuo de la segunda congruencia
        self.m2 = m2  # Módulo de la segunda congruencia
    
    def extended_gcd(self, a, b):
        """Función que devuelve el máximo común divisor de a y b, junto con los coeficientes de Bézout"""
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = self.extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
    
    def mod_inverse(self, a, m):
        """Función que devuelve el inverso multiplicativo de a módulo m"""
        gcd, x, y = self.extended_gcd(a, m)
        if gcd != 1:
            raise Exception("El inverso modular no existe")
        else:
            return x % m
    
    def find_min_n(self):
        """Función que resuelve el sistema de congruencias usando el Teorema Chino del Resto"""
        # Paso 1: Encontrar el inverso multiplicativo de m1 módulo m2
        m1_inv = self.mod_inverse(self.m1, self.m2)
        
        # Paso 2: Resolver la congruencia
        k = (self.a2 - self.a1) * m1_inv % self.m2
        
        # Paso 3: Calcular n
        n = self.m1 * k + self.a1
        return n

def main():
    print("Resolviendo el sistema de congruencias:")
    divisor1 = int(input("Ingrese el primer divisor (m1): "))
    constant1 = int(input(f"Ingrese la constante sumada a n en la primera congruencia (por ejemplo, 4 si es n+4) para m1 = {divisor1}: "))
    
    divisor2 = int(input("Ingrese el segundo divisor (m2): "))
    constant2 = int(input(f"Ingrese la constante sumada a n en la segunda congruencia (por ejemplo, 2 si es n+2) para m2 = {divisor2}: "))
    
    # Calculamos los residuos a1 y a2
    a1 = (divisor1 - constant1) % divisor1
    a2 = (divisor2 - constant2) % divisor2
    
    # Crear una instancia de la clase con los parámetros del problema
    crt = ChineseRemainderTheorem(a1, divisor1, a2, divisor2)

    # Encontrar el menor entero positivo n que satisface ambas congruencias
    n = crt.find_min_n()
    print(f"\nEl menor entero positivo n que satisface ambas congruencias es: {n}")

if __name__ == "__main__":
    main()
