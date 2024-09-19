# src/logic/sat_solver.py

from sympy import symbols, And, Or, Not
from sympy.logic.boolalg import to_cnf
from pysat.solvers import Glucose3

def is_satisfiable(expr):
    """
    Verifica si una expresión lógica es satisfacible usando el solver SAT.

    Args:
        expr (sympy.Expr): La expresión lógica en SymPy.
    
    Returns:
        str: 'SAT' si es satisfacible, 'UNSAT' si no lo es.
    """
    # Convertimos la expresión a su forma normal conjuntiva (CNF)
    cnf_expr = to_cnf(expr, simplify=True)
    
    # Extraemos los símbolos (variables) de la expresión
    symbols_list = sorted(cnf_expr.free_symbols, key=lambda x: str(x))  # Asegurarnos de obtener todas las variables

    # Creamos un mapa de las variables a números para el solver SAT
    var_map = {symbol: i + 1 for i, symbol in enumerate(symbols_list)}

    # Generamos las cláusulas para el solver SAT
    clauses = []

    def convert_to_clauses(expr):
        """
        Convierte una expresión lógica CNF en una lista de cláusulas para el solver SAT.
        """
        if isinstance(expr, And):
            for arg in expr.args:
                convert_to_clauses(arg)
        elif isinstance(expr, Or):
            clause = []
            for arg in expr.args:
                if isinstance(arg, Not):
                    clause.append(-var_map[arg.args[0]])
                else:
                    clause.append(var_map[arg])
            clauses.append(clause)
        elif isinstance(expr, Not):
            clauses.append([-var_map[expr.args[0]]])
        else:
            clauses.append([var_map[expr]])

    # Convertimos la expresión CNF en cláusulas
    convert_to_clauses(cnf_expr)

    # Usamos el solver Glucose3 para determinar la satisfacibilidad
    solver = Glucose3()
    for clause in clauses:
        solver.add_clause(clause)
    
    # Verificamos si la expresión es satisfacible
    satisfiable = solver.solve()
    solver.delete()  # Liberar recursos del solver

    return 'SAT' if satisfiable else 'UNSAT'
