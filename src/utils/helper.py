# src/utils/helper.py
import click

# Mensaje de bienvenida retro
def print_welcome_message():
    """
    Prints a welcome message for the DiscreTools application.
    The welcome message includes:
    - An ASCII art banner for DiscreTools.
    - A brief introduction to the tool.
    - A list of available sections and their respective commands:
    For more details on each section, users are advised to use the --help option.
    """
    
    welcome_message = """
    ============================================================================
    8888b.  88 .dP"Y8  dP""b8 88""Yb 888888 888888  dP"Yb   dP"Yb  88     .dP"Y8
     8I  Yb 88 `Ybo." dP   `" 88__dP 88__     88   dP   Yb dP   Yb 88     `Ybo."
     8I  dY 88 o.`Y8b Yb      88"Yb  88""     88   Yb   dP Yb   dP 88  .o o.`Y8b
    8888Y"  88 8bodP'  YboodP 88  Yb 888888   88    YbodP   YbodP  88ood8 8bodP'                   
    ============================================================================
    Bienvenido a DiscreTools - Tu Herramienta para Matemáticas Discretas
    
    Secciones Disponibles:
    
    1. Lógica Proposicional:
        - evaluate       : Evalúa una expresión lógica con asignaciones
        - table          : Genera una tabla de verdad
        - simplify       : Simplifica una expresión lógica a DNF o CNF
        - classify       : Clasifica una expresión como tautología, contradicción o contingencia
        - equivalent     : Verifica si dos expresiones son equivalentes

    2. Herramientas Comunes:
        - gcd-command    : Calcula el Máximo Común Divisor (MCD)
        - lcm-command    : Calcula el Mínimo Común Múltiplo (MCM)
        - primes         : Genera números primos menores o iguales a n
        - congruence     : Verifica si dos números son congruentes (mod m)
        - solve-congruence: Resuelve la congruencia lineal ax ≡ b (mod m)
        - solve-diophantine-command : Resuelve la ecuación diofántica ax + by = c
    
    Para más detalles, usa --help en cada sección.
    =====================================================
    """
    click.echo(welcome_message)


@click.group()
def cli():
    """Aplicación para Matemáticas Discretas 2"""
    print_welcome_message()


@cli.group()
def logic():
    """Operaciones de Lógica Proposicional"""
    # Aquí van los comandos definidos para lógica proposicional

@cli.group()
def common_tools():
    """Herramientas comunes de Matemáticas Discretas"""
    # Aquí van los comandos definidos para herramientas comunes

# Aquí van los comandos definidos como antes, en logic y common_tools

if __name__ == '__main__':
    cli()
