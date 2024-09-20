""" Módulo principal de la aplicación. """
# src/cli.py

import click
from src.common_tools.common_tools_cli import common_tools_cli
from src.logic.logic_cli import logic_cli

@click.group()
def cli():
    """Aplicación principal de Matemáticas Discretas 2."""
    pass

# Registrar los subcomandos
cli.add_command(common_tools_cli, name='common_tools')
cli.add_command(logic_cli, name='logic')

if __name__ == "__main__":
    cli()
