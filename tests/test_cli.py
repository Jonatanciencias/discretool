# tests/test_cli.py
import unittest
from click.testing import CliRunner
from src.cli import cli

class TestCLI(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_welcome_message(self):
        """Probar que el mensaje de bienvenida se muestra al ejecutar sin comandos"""
        result = self.runner.invoke(cli)
        assert "Bienvenido a DiscreTools" in result.output
        assert result.exit_code == 0

    def test_evaluate_command(self):
        """Probar la evaluación de una expresión lógica"""
        result = self.runner.invoke(cli, ['logic', 'evaluate', '(A -> B)', '-a', 'A', 'True', '-a', 'B', 'False'])
        assert "Resultado: False" in result.output
        assert result.exit_code == 0

    def test_gcd_command(self):
        """Probar el cálculo del MCD"""
        result = self.runner.invoke(cli, ['common_tools', 'gcd-command', '60', '48'])
        assert "El MCD de 60 y 48 es 12" in result.output
        assert result.exit_code == 0

if __name__ == '__main__':
    unittest.main()
