"""Módulo principal de la aplicación."""
# src/cli.py

import click
from src.common_tools.common_tools_cli import common_tools_cli
from src.logic.logic_cli import logic_cli
from src.utils.helper import print_welcome_message
from src.combinatorics.combinatorics_cli import combinatorics_cli  # Import corregido

@click.group(invoke_without_command=True)
@click.option('--home', is_flag=True, help="Muestra la página principal de bienvenida.")
@click.pass_context
def cli(ctx, home):
    """Aplicación principal de Matemáticas Discretas 2."""
    if home:
        print_welcome_message()
    elif ctx.invoked_subcommand is None:  # Solo muestra el mensaje si no hay un subcomando ejecutado
        click.echo("Usa --help para ver los comandos disponibles.")


# Registrar los subcomandos
cli.add_command(common_tools_cli, name='common_tools')
cli.add_command(logic_cli, name='logic')
cli.add_command(combinatorics_cli, name="combinatorics")

if __name__ == "__main__":
    cli()
