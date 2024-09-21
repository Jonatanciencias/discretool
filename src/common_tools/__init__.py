""" This module contains the common tools used in number theory. """
# src/common_tools/__init__.py

from .congruences import (
    is_congruent,
    solve_linear_congruence,
    solve_diophantine
)

from .gcd_lcm import (
    gcd,
    lcm,
    division_algorithm,
    extended_gcd
)

from .prime_tools import (
    generate_primes,
)

from .prime_factorization import (
    factorize,
)

from .modular_arithmetic import (
    mod_exp,
    mod_inverse
)

__all__ = [
    "is_congruent",
    "solve_linear_congruence",
    "solve_diophantine",
    "gcd",
    "lcm",
    "division_algorithm",
    "generate_primes",
    "factorize",
    "mod_exp",
    "mod_inverse",
    "extended_gcd"
]

config = {
    "version": "1.0.0",
    "author": "Jonatan García"
}