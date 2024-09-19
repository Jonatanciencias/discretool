# src/common_tools/__init__.py

from .congruences import (
    is_congruent,
    solve_linear_congruence,
    solve_diophantine
)

from .gcd_lcm import (
    gcd,
    lcm,
    division_algorithm
)

from .prime_tools import (
    generate_primes,
)

__all__ = [
    "is_congruent",
    "solve_linear_congruence",
    "solve_diophantine",
    "gcd",
    "lcm",
    "division_algorithm",
    "generate_primes"
]
