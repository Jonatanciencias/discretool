""" Este módulo contiene funciones para generar permutaciones y combinaciones de un conjunto de elementos. """
# src/combinatorics/__init__.py

from .permutations import permutations, circular_permutations, generalized_binomial
from .combinations import combinations
from .combinations_with_repetition import combinations_with_repetition
from .subsets import generate_subsets
from .multinomial import multinomial
from .stirling_numbers import stirling_first, stirling_second
from .catalan_numbers import catalan_number
from .partitions import generate_partitions
from .lexicographic_combinations import generate_lexicographic_combinations
from . heap_permutations import heap_permutations

__all__ = [
    "permutations",
    "combinations",
    "combinations_with_repetition",
    "circular_permutations",
    "generalized_binomial",
    "generate_subsets",
    "multinomial",
    "stirling_first",
    "stirling_second",
    "catalan_number",
    "generate_partitions",
    "generate_lexicographic_combinations",
    "heap_permutations"
    
]