""" Este módulo contiene funciones para generar permutaciones y combinaciones de un conjunto de elementos. """
# src/combinatorics/__init__.py

from .permutations import permutations
from .combinations import combinations

__all__ = [
    'permutations',
    'combinations'
]