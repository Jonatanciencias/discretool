""" Módulo con funciones de ayuda para la aplicación. """
# src/utils/helper.py

import click

def print_welcome_message():
    """
    Muestra un mensaje de bienvenida con un menú detallado de las secciones
    y sus comandos disponibles.
    """
    welcome_message = """
    ============================================================================   
    8888b.  88 .dP"Y8  dP""b8 88""Yb 888888 888888  dP"Yb   dP"Yb  88     .dP"Y8
     8I  Yb 88 `Ybo." dP   `" 88__dP 88__     88   dP   Yb dP   Yb 88     `Ybo."
     8I  dY 88 o.`Y8b Yb      88"Yb  88""     88   Yb   dP Yb   dP 88  .o o.`Y8b
    8888Y"  88 8bodP'  YboodP 88  Yb 888888   88    YbodP   YbodP  88ood8 8bodP'                   
    ============================================================================
    Bienvenido a DiscreTool - Tu Herramienta para Matemáticas Discretas
    
    Secciones Disponibles:
    
    1. Lógica Proposicional:
        - evaluate       : Evalúa una expresión lógica con asignaciones.
        - table          : Genera una tabla de verdad.
        - simplify       : Simplifica una expresión lógica a DNF o CNF.
        - classify       : Clasifica una expresión como tautología, contradicción o contingencia.
        - equivalent     : Verifica si dos expresiones son equivalentes.
    
    2. Herramientas Comunes:
        - gcd                       : Calcula el Máximo Común Divisor (MCD).
        - lcm                       : Calcula el Mínimo Común Múltiplo (MCM).
        - generate_primes           : Genera números primos menores o iguales a un número dado.
        - is_congruent              : Verifica si dos números son congruentes bajo un módulo.
        - solve_linear_congruence   : Resuelve la congruencia ax ≡ b (mod m).
        - solve_diophantine         : Resuelve ecuaciones diofánticas del tipo ax + by = c.
    
    3. Combinatoria (Próximamente):
        - combinations   : Calcula combinaciones.
        - permutations   : Calcula permutaciones.
    
    4. Grafos (Próximamente):
        - shortest-path  : Encuentra el camino más corto en un grafo.
        - detect-cycle   : Detecta ciclos en un grafo.
    
    5. Recursión (Próximamente):
        - factorial      : Calcula el factorial de un número usando recursión.
        - fibonacci      : Calcula la secuencia de Fibonacci de forma recursiva.
    
    Usa --help en cualquier comando para más detalles.
    ============================================================================
    """
    click.echo(welcome_message)


@click.group()
def cli():
    """Aplicación para resolver problemas de Matemáticas Discretas."""
    print_welcome_message()

@cli.group()
def logic():
    """Operaciones de Lógica Proposicional"""
    pass  # Aquí se definen los comandos de lógica proposicional

@cli.group()
def common_tools():
    """Herramientas Comunes de Matemáticas Discretas"""
    pass  # Aquí se definen los comandos de herramientas comunes

@cli.group()
def combinatorics():
    """Operaciones de Combinatoria (Próximamente)"""
    pass

@cli.group()
def graphs():
    """Operaciones con Grafos (Próximamente)"""
    pass

@cli.group()
def recursion():
    """Operaciones de Recursión (Próximamente)"""
    pass

if __name__ == '__main__':
    cli()
