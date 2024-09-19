'''
Un entero positivo n deja residuo 4 cuando se divide
por 5. Entonces el residuo que se obtiene cuando se
divide a 6n+1 por 5 es:
'''

class ModuloOperation:
    def __init__(self, n):
        self.n = n
    
    def calculate_remainder(self, divisor):
        return self.n % divisor
    
    def expression_remainder(self):
        expression_result = 6 * self.n + 1
        return expression_result % 5

# Crear una instancia de ModuloOperation con un n que deje residuo 4 al dividirse por 5
n = 4  # Ejemplo de n que deja residuo 4 al dividirse por 5
operation = ModuloOperation(n)

# Calcular el residuo de 6n + 1 al dividirse por 5
remainder = operation.expression_remainder()
remainder
