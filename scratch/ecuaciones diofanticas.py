def extended_gcd(a, b):
    """
    Algoritmo de Euclides extendido.
    Retorna gcd(a, b) y los coeficientes x e y que satisfacen ax + by = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def solve_diofantica(a, b, c):
    """
    Resuelve la ecuación diofántica ax + by = c.
    Retorna una solución particular (x, y) si existe.
    """
    gcd, x, y = extended_gcd(a, b)
    
    # c debe ser divisible por gcd(a, b) para que haya solución
    if c % gcd != 0:
        return None  # No hay solución
    
    # Escalar la solución para obtener el valor correcto de c
    factor = c // gcd
    x *= factor
    y *= factor
    
    return x, y

def get_numbers():
    """
    Función para obtener los valores de a, b y c desde el usuario.
    """
    print("ax + by = c")
    a = int(input("Coeficiente a: "))
    b = int(input("Coeficiente b: "))
    c = int(input("Coeficiente c: "))
    return a, b, c

# Descomponer la tupla de retorno de get_numbers()
a, b, c = get_numbers()

# Resolver la ecuación diofántica con los valores ingresados
solucion = solve_diofantica(a, b, c)

if solucion:
    print(f"Una solución es x = {solucion[0]}, y = {solucion[1]}")
else:
    print("No hay solución")
