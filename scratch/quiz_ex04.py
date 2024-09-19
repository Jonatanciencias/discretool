'''
EI máximo común divisor de dos números
enteros positivos menores que 400 es igual a 8,
Su mínimo común múltiplo es 15 veces uno de los
enteros. ¿Cuál es la suma más grande posible de
los dos enteros?
'''
import math

class MaxSumOfIntegers:
    def __init__(self, max_value, gcd_value, lcm_multiplier):
        self.max_value = max_value  # El valor máximo permitido para a y b
        self.gcd_value = gcd_value  # El MCD que se debe cumplir
        self.lcm_multiplier = lcm_multiplier  # Multiplicador del MCM

    def find_max_sum(self):
        max_sum = 0
        best_pair = (0, 0)
        
        # Iterar sobre todos los posibles pares (a, b)
        for a in range(self.gcd_value, self.max_value, self.gcd_value):
            for b in range(a, self.max_value, self.gcd_value):
                if math.gcd(a, b) == self.gcd_value:
                    lcm = (a * b) // math.gcd(a, b)
                    if lcm == self.lcm_multiplier * min(a, b):
                        current_sum = a + b
                        if current_sum > max_sum:
                            max_sum = current_sum
                            best_pair = (a, b)
        
        return best_pair, max_sum

def main():
    print("Resolviendo el problema de suma máxima:")
    
    max_value = int(input("Ingrese el valor máximo permitido para a y b (por ejemplo, 400): "))
    gcd_value = int(input("Ingrese el MCD deseado (por ejemplo, 8): "))
    lcm_multiplier = int(input("Ingrese el multiplicador del MCM (por ejemplo, 15): "))
    
    # Crear una instancia de la clase con los parámetros del problema
    max_sum_finder = MaxSumOfIntegers(max_value, gcd_value, lcm_multiplier)

    # Encontrar los enteros que satisfacen las condiciones
    best_pair, max_sum = max_sum_finder.find_max_sum()
    print(f"\nLa suma más grande posible de los dos enteros es {max_sum}, y se obtiene con los números {best_pair[0]} y {best_pair[1]}.")

if __name__ == "__main__":
    main()
