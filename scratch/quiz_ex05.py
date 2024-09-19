class ResiduoCalculator:
    def __init__(self, n):
        self.n = n

    def residuo_division(self, divisor):
        """Método para calcular el residuo de una división"""
        return self.n % divisor

    def calcular_residuo_3n_mas_7(self, divisor):
        """Método para calcular el residuo de 3n + 7 dividido por el divisor"""
        resultado = 3 * self.n + 7
        return resultado % divisor

# Crear una instancia de la clase con n = 6
n = 6
divisor = 9
calculador = ResiduoCalculator(n)

# Calcular el residuo de 3n + 7 cuando se divide por 9
residuo = calculador.calcular_residuo_3n_mas_7(divisor)
print(f"El residuo de 3n + 7 cuando n = {n} se divide por {divisor} es: {residuo}")
