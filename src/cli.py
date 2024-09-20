# src/cli.py

import click
from src.common_tools.common_tools_cli import common_tools_cli
from src.logic.logic_cli import logic_cli
# Otros CLIs futuros (combinatorics, graphs, recursion) se importarán aquí

@click.group()
def cli():
    """Aplicación principal de Matemáticas Discretas 2."""
    pass

# Registrar los subcomandos importando cada CLI como un grupo
cli.add_command(common_tools_cli, name='common_tools')
cli.add_command(logic_cli, name='logic')

# A futuro, si añades más secciones como combinatorics, graphs, recursion
# cli.add_command(combinatorics_cli, name='combinatorics')
# cli.add_command(graphs_cli, name='graphs')
# cli.add_command(recursion_cli, name='recursion')

if __name__ == "__main__":
    cli()
