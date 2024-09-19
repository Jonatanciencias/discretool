""" Módulo con las reglas de inferencia lógica. """
from sympy import Implies, Or, Not

# Definición de las reglas de inferencia
def modus_ponens(implication, premise):
    """
    Aplica Modus Ponens: Si A -> B y A, entonces B.
    """
    if isinstance(implication, Implies) and implication.args[0] == premise:
        return implication.args[1]  # Retorna B
    return None

def modus_tollens(implication, neg_consequence):
    """
    Aplica Modus Tollens: Si A -> B y ~B, entonces ~A.
    """
    if isinstance(implication, Implies) and isinstance(neg_consequence, Not) and implication.args[1] == neg_consequence.args[0]:
        return Not(implication.args[0])  # Retorna ~A
    return None

def disjunctive_syllogism(disjunction, neg_disjunct):
    """
    Aplica el Silogismo Disyuntivo: Si A v B y ~A, entonces B.
    """
    if isinstance(disjunction, Or):
        if disjunction.args[0] == neg_disjunct.args[0] and isinstance(neg_disjunct, Not):
            return disjunction.args[1]  # Retorna B
        elif disjunction.args[1] == neg_disjunct.args[0] and isinstance(neg_disjunct, Not):
            return disjunction.args[0]  # Retorna A
    return None

def hypothetical_syllogism(implication1, implication2):
    """
    Aplica el Silogismo Hipotético: Si A -> B y B -> C, entonces A -> C.
    """
    if isinstance(implication1, Implies) and isinstance(implication2, Implies) and implication1.args[1] == implication2.args[0]:
        return Implies(implication1.args[0], implication2.args[1])  # Retorna A -> C
    return None

def double_negation(negation):
    """
    Aplica la Doble Negación: Si ~~A, entonces A.
    """
    if isinstance(negation, Not) and isinstance(negation.args[0], Not):
        return negation.args[0]  # Retorna A
    return None
