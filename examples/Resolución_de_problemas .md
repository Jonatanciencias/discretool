## 1. Lógica Proposicional: 

Para determinar qué equipos son aptos para resolver problemas lógicos, se presentan las siguientes expresiones lógicas, y se pide que se clasifiquen como tautología, contradicción, o contingencia:

- (A∧B)→C
- A∨¬A
- (P∧Q)↔(¬P∨¬Q)

### Resolución del Problema con DiscreTool

#### Resolver la Clasificación Lógica

Utilizamos la sección de lógica proposicional para determinar si las expresiones son tautologías, contradicciones, o contingencias.

```bash
# Clasificar la primera expresión lógica
python -m src.cli logic classify "(A ∧ B) → C"

# Clasificar la segunda expresión lógica
python -m src.cli logic classify "A ∨ ¬A"

# Clasificar la tercera expresión lógica
python -m src.cli logic classify "(P ∧ Q) ↔ (¬P ∨ ¬Q)"
```

## 2. Combinatoria 

De un grupo de 10 estudiantes, el profesor seleccionará equipos de 3 estudiantes. Se permite la repetición de estudiantes en diferentes equipos. Además, se pide determinar cuántas permutaciones circulares se pueden hacer entre 5 estudiantes para resolver problemas en una mesa redonda.

#### Calcular las Combinaciones y Permutaciones

En esta parte, utilizamos la sección de combinatoria para resolver la selección de equipos de 3 estudiantes y calcular las permutaciones circulares de 5 estudiantes.

```bash
# Calcular combinaciones de 10 estudiantes tomados de 3 con repetición
python -m src.cli combinatorics combinations_with_repetition 10 3

# Calcular permutaciones circulares de 5 estudiantes
python -m src.cli combinatorics circular_permutations 5
```

## 3. Aritmética Modular

Un equipo de 5 estudiantes recibe la tarea de resolver una serie de ecuaciones modulares. Deben verificar si los siguientes números son congruentes entre sí y, además, resolver una ecuación modular

- Verificar si $35≡5(mod 10)$
- Resolver la congruencia $14𝑥≡30 (mod 100)$

### Resolver los Problemas de Aritmética Modular

Ahora, pasamos a la sección de common tools para verificar la congruencia y resolver la ecuación modular.

```bash
# Verificar si 35 es congruente con 5 módulo 10
python -m src.cli common_tools is_congruent 35 5 10

# Resolver la ecuación modular 14x ≡ 30 (mod 100)
python -m src.cli common_tools solve_linear_congruence 14 30 100
```

## 4. Combinatoria Avanzada

El profesor quiere calcular cuántas maneras puede dividir a los 10 estudiantes en 3 grupos con tamaños diferentes para distribuir las tareas. Además, quiere generar todas las permutaciones posibles de los estudiantes en un orden particula

### Resolver la Distribución de Grupos y Permutaciones

Finalmente, resolvemos cuántas maneras puede el profesor dividir a los 10 estudiantes en 3 grupos con tamaños diferentes y generamos todas las permutaciones posibles en un orden particular.

```bash
# Calcular el coeficiente multinomial para dividir 10 estudiantes en 3 grupos de tamaños diferentes
python -m src.cli combinatorics multinomial 10 3 3 4

# Generar todas las permutaciones posibles de los 10 estudiantes
python -m src.cli combinatorics heap_permutations 10
```