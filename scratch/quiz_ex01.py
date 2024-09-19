'''
El máximo común divisor de dos números enteros positivos
menores que 303 es igual a 4, Su mínimo común múltiplo es
10 veces uno de los enteros. ¿Cuál es la suma más grande
posible de los dos enteros?
'''

import math

class NumberPair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def gcd(self):
        return math.gcd(self.a, self.b)
    
    def lcm(self):
        return abs(self.a * self.b) // self.gcd()
    
    def meets_conditions(self):
        return self.gcd() == 4 and (self.lcm() == 10 * self.a or self.lcm() == 10 * self.b)
    
    def sum(self):
        return self.a + self.b

def find_max_sum(limit):
    max_sum = 0
    best_pair = None
    
    for a in range(4, limit, 4):  # a must be a multiple of 4
        for b in range(4, limit, 4):  # b must be a multiple of 4
            pair = NumberPair(a, b)
            if pair.meets_conditions() and pair.sum() > max_sum:
                max_sum = pair.sum()
                best_pair = pair
    
    return best_pair

# Ejecución
limit = 303
best_pair = find_max_sum(limit)
if best_pair:
    print(f"La mejor pareja es: a = {best_pair.a}, b = {best_pair.b}")
    print(f"La suma más grande posible es: {best_pair.sum()}")
else:
    print("No se encontró ninguna pareja que cumpla las condiciones.")
