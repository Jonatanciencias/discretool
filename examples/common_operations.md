1. GCD (Greatest Common Divisor)

```bash
python -m src.cli common_tools gcd 48 180
python -m src.cli common_tools gcd 128 64
python -m src.cli common_tools gcd 54 24
python -m src.cli common_tools gcd 101 103  # Primos
```

2. LCM (Least Common Multiple)

```bash
python -m src.cli common_tools lcm 48 180
python -m src.cli common_tools lcm 128 64
python -m src.cli common_tools lcm 54 24
python -m src.cli common_tools lcm 101 103  # Primos
```

3. Verificación de Congruencia

```bash
python -m src.cli common_tools is_congruent 17 5 3
python -m src.cli common_tools is_congruent 12 15 5
python -m src.cli common_tools is_congruent 100 40 6
python -m src.cli common_tools is_congruent 123 123 7
```

4. Solución de Congruencias Lineales

```bash
python -m src.cli common_tools solve_linear_congruence 3 4 7
python -m src.cli common_tools solve_linear_congruence 10 5 8
python -m src.cli common_tools solve_linear_congruence 15 5 6
python -m src.cli common_tools solve_linear_congruence 17 9 20
```

5. Generación de Primos

```bash
python -m src.cli common_tools generate_primes 10
python -m src.cli common_tools generate_primes 50
python -m src.cli common_tools generate_primes 100
```

6. Evaluación de Expresiones Lógicas

```bash
python -m src.cli logic evaluate "A ∧ B → C" -a A True -a B False -a C True
python -m src.cli logic evaluate "¬A ∨ B" -a A False -a B True
python -m src.cli logic evaluate "A ↔ B" -a A True -a B False
python -m src.cli logic evaluate "(A ∧ B) ∨ ¬C" -a A True -a B True -a C False
```

7. Simplificación de Expresiones Lógicas

```bash
python -m src.cli logic simplify "A ∧ (B ∨ ¬C)" -f cnf
python -m src.cli logic simplify "A ∧ B ∨ ¬A" -f dnf
python -m src.cli logic simplify "A ∨ (¬A ∧ B)" -f cnf
```

8. Clasificación de Expresiones

```bash
python -m src.cli logic classify "A ∧ (B ∨ ¬B)"
python -m src.cli logic classify "A ∨ ¬A"
python -m src.cli logic classify "A ↔ A"
```

9. Verificación de Equivalencia Lógica

```bash
python -m src.cli logic equivalent "A ∧ (B ∨ C)" "B ∧ A ∨ C"
python -m src.cli logic equivalent "A ↔ B" "B ↔ A"
python -m src.cli logic equivalent "(A ∨ B) ∧ C" "A ∧ (B ∨ C)"
```

10. Generación de Tablas de Verdad

```bash
python -m src.cli logic table "A ∨ B"
python -m src.cli logic table "A ∧ B → C" --export csv --filename truth_table_test
python -m src.cli logic table "A ∧ B" --export md --filename truth_table_test_md
python -m src.cli logic table "¬A ∧ B" --graph
python -m src.cli logic table "A ∧ B" --graph --filename table_graph

```

11. Resolución de Ecuaciones Diofánticas

```bash
python -m src.cli common_tools solve_diophantine 3 5 7
python -m src.cli common_tools solve_diophantine 10 4 6
python -m src.cli common_tools solve_diophantine 15 9 3
```
