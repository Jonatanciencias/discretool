# tests/test_logic_solver.py

import unittest
from src.logic.logic_solver import (
    parse_expression,
    evaluate_expression,
    truth_table,
    simplify_expression,
    classify_expression,
    are_equivalent
)

class TestLogicSolver(unittest.TestCase):

    def test_parse_expression(self):
        expr_str = "A & B"
        expr = parse_expression(expr_str)
        self.assertEqual(expr, parse_expression("(A & B)"))

    def test_evaluate_expression(self):
        expr = parse_expression("A | B")
        assignments = {'A': False, 'B': True}
        result = evaluate_expression(expr, assignments)
        self.assertTrue(result)

    def test_truth_table(self):
        expr = parse_expression("A & B")
        headers, table = truth_table(expr)
        self.assertEqual(len(table), 4)
        self.assertEqual(table[0]['A & B'], False)
        self.assertEqual(table[3]['A & B'], True)

    def test_simplify_expression(self):
        expr = parse_expression("A & (A | B)")
        simplified = simplify_expression(expr, form='dnf')
        self.assertEqual(str(simplified), "A")

    def test_classify_expression(self):
        expr = parse_expression("A | ~A")
        classification = classify_expression(expr)
        self.assertEqual(classification, "Tautología")
        
        expr = parse_expression("A & ~A")
        classification = classify_expression(expr)
        self.assertEqual(classification, "Contradicción")
        
        expr = parse_expression("A & B")
        classification = classify_expression(expr)
        self.assertEqual(classification, "Contingencia")

    def test_are_equivalent(self):
        expr1 = parse_expression("A & B")
        expr2 = parse_expression("B & A")
        self.assertTrue(are_equivalent(expr1, expr2))
        
        expr1 = parse_expression("A | (B & C)")
        expr2 = parse_expression("(A | B) & (A | C)")
        self.assertTrue(are_equivalent(expr1, expr2))

if __name__ == '__main__':
    unittest.main()
