def encontrar_congruente(a, mod, exp=None):
    if exp is None:
        # Si no hay exponente, lo tratamos como 1
        exp = 1
    else:
        # Asegurarse de que exp es un número entero
        exp = int(exp)

    # Aplicar la exponenciación modular para evitar el overflow
    a_mod = pow(a, exp, mod)

    # Generar una lista de posibles soluciones congruentes con a_mod (dentro del rango del mod)
    soluciones = [(a_mod + mod * k) for k in range(-5, 6)]  # Genera 11 soluciones: desde k = -5 hasta k = 5

    # Sugerir el número más cercano a cero como recomendado
    recomendado = min(soluciones, key=abs)

    # Mostrar resultados
    print(f"Número a: {a}")
    print(f"Módulo: {mod}")
    print("Posibles números congruentes:")
    print(soluciones)
    print(f"Número recomendado: {recomendado}")

    return soluciones, recomendado

# Solicitar entrada del usuario
a = int(input("Ingresa el número a: "))
exp_input = input("Ingresa el exponente (deja en blanco si no tiene): ")
exp = float(exp_input) if exp_input else None
mod = int(input("Ingresa el módulo: "))

# Llamar a la función
soluciones, recomendado = encontrar_congruente(a, mod, exp)
