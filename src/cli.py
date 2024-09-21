"""Módulo principal de la aplicación."""
# src/cli.py

import click
from src.common_tools.common_tools_cli import common_tools_cli
from src.logic.logic_cli import logic_cli
from src.utils.helper import print_welcome_message
from src.combinatorics import combinatorics_cli

@click.group(invoke_without_command=True)
@click.option('--home', is_flag=True, help="Muestra la página principal de bienvenida.")
def cli(home):
    """Aplicación principal de Matemáticas Discretas 2."""
    if home:
        print_welcome_message()
    elif not home:
        click.echo("Usa --help para ver los comandos disponibles.")


# Registrar los subcomandos
cli.add_command(common_tools_cli, name='common_tools')
cli.add_command(logic_cli, name='logic')
cli.add_command(combinatorics_cli, name="combinatorics")

if __name__ == "__main__":
    cli()
