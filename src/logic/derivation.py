# src/logic/derivation.py

from sympy import Implies, Or, Not
from .inference import modus_ponens, modus_tollens, disjunctive_syllogism, hypothetical_syllogism, double_negation

def apply_inference_rules(steps):
    """
    Aplica reglas de inferencia a un conjunto de pasos lógicos.
    
    Args:
        steps (list): Lista de premisas o inferencias (proposiciones lógicas).
        
    Returns:
        list: Lista de pasos deducidos.
    """
    deductions = []
    
    for i, step in enumerate(steps):
        # Compara cada paso con los anteriores para aplicar las reglas
        for j in range(i):
            previous_step = steps[j]
            
            # Aplica Modus Ponens
            result = modus_ponens(previous_step, step)
            if result is not None:
                deductions.append(f"Modus Ponens: {previous_step} y {step} => {result}")
                steps.append(result)
            
            # Aplica Modus Tollens
            result = modus_tollens(previous_step, step)
            if result is not None:
                deductions.append(f"Modus Tollens: {previous_step} y {step} => {result}")
                steps.append(result)
            
            # Aplica Silogismo Disyuntivo
            result = disjunctive_syllogism(previous_step, step)
            if result is not None:
                deductions.append(f"Silogismo Disyuntivo: {previous_step} y {step} => {result}")
                steps.append(result)
            
            # Aplica Silogismo Hipotético
            result = hypothetical_syllogism(previous_step, step)
            if result is not None:
                deductions.append(f"Silogismo Hipotético: {previous_step} y {step} => {result}")
                steps.append(result)
            
            # Aplica Doble Negación
            result = double_negation(step)
            if result is not None:
                deductions.append(f"Doble Negación: {step} => {result}")
                steps.append(result)
    
    return deductions
