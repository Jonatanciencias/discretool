
1. Combinaciones

Combinaciones de 5 elementos tomados de 3 en 3
```bash
python -m src.cli combinatorics combinations 5 3
```

Combinaciones de 7 elementos tomados de 3 en 3
```bash
python -m src.cli combinatorics combinations 7 3
```

Combinaciones de 10 elementos tomados de 5 en 5
```bash
python -m src.cli combinatorics combinations 10 5
```

Combinaciones de 8 elementos tomados de 2 en 2
```bash
python -m src.cli combinatorics combinations 8 2
```

2. Permutaciones

Permutaciones de 4 elementos tomados de 2 en 2
```bash
python -m src.cli combinatorics permutations 4 2
```

Permutaciones de 6 elementos tomados de 4 en 4
```bash
python -m src.cli combinatorics permutations 6 4
```
Permutaciones de 3 elementos tomados de 3 en 3
```bash
python -m src.cli combinatorics permutations 3 3
```

Permutaciones de 5 elementos tomados de 1 en 1
```bash
python -m src.cli combinatorics permutations 5 1
```

3. Combinaciones con repeticiones

```bash
python -m src.cli combinatorics combinations_with_repetition 5 3
```

4. Permutaciones Circulares

```bash
python -m src.cli combinatorics circular_permutations 5
```

5. Coeficiente Binomial Generalizado

```bash
python -m src.cli combinatorics generalized_binomial 2.5 3
```

6. Subconjuntos de un conjunto de n elementos

```bash
python -m src.cli combinatorics subsets 3
```

```bash
python -m src.cli combinatorics subsets 0
```

7. Coeficiente Multinomial

Prueba con 10 objetos distribuidos en grupos de 3, 2 y 5:

```bash
python -m src.cli combinatorics multinomial 10 3 2 5
```

8. Números de Stirling

```bash
python -m src.cli combinatorics stirling_first 5 3
```
```bash
python -m src.cli combinatorics stirling_second 5 3
```

9. Números de Catalan

```bash
python -m src.cli combinatorics catalan_number 5
```
10. Generación de Particiones

```bash
python -m src.cli combinatorics partitions 5
```