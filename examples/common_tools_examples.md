1. Máximo Común Divisor (MCD)
El MCD de dos números enteros es el mayor número que divide a ambos sin dejar residuo.

```bash
python -m src.cli common_tools gcd 48 180
python -m src.cli common_tools gcd 56 98
python -m src.cli common_tools gcd 123 321
```

2. Mínimo Común Múltiplo (MCM)
El MCM de dos números es el menor múltiplo común de ambos números.

```bash
python -m src.cli common_tools lcm 48 180
python -m src.cli common_tools lcm 21 6
python -m src.cli common_tools lcm 15 25
```

3. Generar Números Primos
Genera todos los números primos hasta un número límite dado.
```bash
python -m src.cli common_tools primes 30
python -m src.cli common_tools primes 50
python -m src.cli common_tools primes 100
```

4. Criba de Eratóstenes
Este algoritmo optimizado genera números primos menores o iguales a un límite dado.

```bash
python -m src.cli common_tools sieve_primes 50
python -m src.cli common_tools sieve_primes 100
python -m src.cli common_tools sieve_primes 200
```

5. Verificar Congruencias
Verifica si dos números son congruentes bajo un módulo específico (a ≡ b mod m).

```bash
python -m src.cli common_tools is_congruent 17 5 3
python -m src.cli common_tools is_congruent 20 7 4
python -m src.cli common_tools is_congruent 15 9 6
```

6. Resolver Congruencias
Resuelve una ecuación de congruencia lineal del tipo ax ≡ b mod m.

```bash
python -m src.cli common_tools solve_linear_congruence 14 30 100
python -m src.cli common_tools solve_linear_congruence 20 15 45
python -m src.cli common_tools solve_linear_congruence 3 6 9
```

7. Factorización Prima
Descompone un número en sus factores primos.

```bash
python -m src.cli common_tools prime_factorization 120
python -m src.cli common_tools prime_factorization 45
python -m src.cli common_tools prime_factorization 200
```

8. Exponenciación Modular
Calcula la exponenciación modular, útil para grandes potencias en aritmética modular.

```bash
python -m src.cli common_tools mod_exp 4 13 497
python -m src.cli common_tools mod_exp 2 5 7
python -m src.cli common_tools mod_exp 10 20 11
```

9. Algoritmo Extendido de Euclides
Este algoritmo encuentra el MCD de dos números y devuelve los coeficientes de Bézout que satisfacen la ecuación ax + by = gcd(a, b).

```bash
python -m src.cli common_tools extended_gcd 56 98
python -m src.cli common_tools extended_gcd 48 18
python -m src.cli common_tools extended_gcd 120 23
```

10. Algoritmo de la División
Calcula el cociente y el residuo de la división entre dos números.

```bash
python -m src.cli common_tools division_alg 10 3
python -m src.cli common_tools division_alg 25 7
python -m src.cli common_tools division_alg 56 5
```

11. Algoritmo Extendido de Euclides (Ejemplo 2)
Calcula el MCD de dos números junto con los coeficientes de Bézout.

```bash
python -m src.cli common_tools extended_gcd 56 15
python -m src.cli common_tools extended_gcd 81 57
python -m src.cli common_tools extended_gcd 98 45
```

