# tests/test_logic_solver.py
import unittest
from sympy import And, symbols
from src.logic import (
    parse_expression,
    evaluate_expression,
    are_equivalent
)


class TestLogicSolver(unittest.TestCase):
    """
    TestLogicSolver is a test case for testing the logic solver functionalities.
    Methods:
        test_parse_expression:
            Tests the parsing of a logical expression and verifies its string representation.
        test_evaluate_expression:
            Tests the evaluation of a parsed logical expression with given variable values and verifies the result.
        test_equivalence:
            Tests the equivalence of two logical expressions by parsing them and verifying if they are logically equivalent.
    """
    
    def test_parse_expression(self):
        """
        Test the parse_expression function.

        This test case verifies that the parse_expression function correctly parses
        a logical expression string and converts it into the expected expression object.

        The test checks if the string representation of the parsed expression matches
        the expected output.

        Assertions:
            - The string representation of the parsed expression should be "And(A, B)".
        """
        # Definir símbolos A y B
        A, B = symbols('A B')
        # Parsear una expresión y comparar con la clase SymPy And
        expr = parse_expression("(A & B)")
        self.assertEqual(expr, And(A, B))  # Comparar con la clase And usando símbolos
    
    def test_evaluate_expression(self):
        """
        Test the evaluate_expression function with a given logical expression.

        This test checks the evaluation of the logical expression "(A & B)" 
        with the provided variable values. Specifically, it verifies that 
        the expression evaluates to False when 'A' is True and 'B' is False.

        Assertions:
            - The result of the evaluation should be False.
        """
        expr = parse_expression("(A & B)")
        result = evaluate_expression(expr, {'A': True, 'B': False})
        self.assertFalse(result)

    def test_equivalence(self):
        """
        Test the equivalence of two logical expressions.

        This test verifies that the logical expressions "(A -> B)" and "(~A | B)"
        are equivalent by parsing them and checking their equivalence using the
        `are_equivalent` function.

        Assertions:
            - The parsed expressions of "(A -> B)" and "(~A | B)" should be equivalent.
        """
        expr1 = parse_expression("(A -> B)")
        expr2 = parse_expression("(~A | B)")
        self.assertTrue(are_equivalent(expr1, expr2))

if __name__ == '__main__':
    unittest.main()
