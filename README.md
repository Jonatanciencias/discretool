    ============================================================================   
    8888b.  88 .dP"Y8  dP""b8 88""Yb 888888 888888  dP"Yb   dP"Yb  88     .dP"Y8
     8I  Yb 88 `Ybo." dP   `" 88__dP 88__     88   dP   Yb dP   Yb 88     `Ybo."
     8I  dY 88 o.`Y8b Yb      88"Yb  88""     88   Yb   dP Yb   dP 88  .o o.`Y8b
    8888Y"  88 8bodP'  YboodP 88  Yb 888888   88    YbodP   YbodP  88ood8 8bodP'                   
    ============================================================================
         Bienvenido a DiscreTool - Tu Herramienta para Matemáticas Discretas

**DiscreTool** es una herramienta CLI (línea de comandos) desarrollada en Python para facilitar la resolución de problemas comunes en Matemáticas Discretas. Incluye funcionalidades para lógica proposicional, operaciones aritméticas, combinatoria, grafos, y recursión.

## Características

### Lógica Proposicional

[logic_examples]()

- **Evaluación de expresiones lógicas**: Evalúa expresiones con asignaciones de verdad a variables proposicionales.
- **Generación de tablas de verdad**: Crea tablas de verdad de cualquier expresión.
- **Simplificación**: Simplifica expresiones en formas normales disyuntivas (DNF) y conjuntivas (CNF).
- **Equivalencia**: Verifica si dos expresiones lógicas son equivalentes.
- **Clasificación**: Clasifica expresiones como tautologías, contradicciones o contingencias.
- **Deducción natural**: Aplica reglas de inferencia (Modus Ponens, Silogismo Disyuntivo) para derivar conclusiones.

### Herramientas Comunes de Matemáticas Discretas

[common_tools_examples]()

- **Cálculo del MCD**: Calcula el máximo común divisor de dos números.
- **Cálculo del MCM**: Calcula el mínimo común múltiplo.
- **Generación de números primos**: Genera números primos hasta un valor especificado.
- **Congruencias**: Verifica si dos números son congruentes en un módulo dado.
- **Ecuaciones diofánticas**: Resuelve ecuaciones del tipo ax + by = c.
- **Aritmética modular**: Realiza operaciones de aritmética modular.
- **Factorización prima**: Descompone un número en sus factores primos.

### Combinatoria

[combinatorics_examples]()

- Calcula combinaciones y permutaciones.

### Próximas Funcionalidades


- **Grafos**: Realiza operaciones sobre grafos, como encontrar el camino más corto.
- **Recursión**: Resuelve problemas utilizando algoritmos recursivos.

## Requisitos

Para ejecutar DiscreTool, necesitarás los siguientes paquetes:

- Python 3.x
- `Click`
- `SymPy`
- `PySAT`

Instala las dependencias con:

```bash
pip install -r requirements.txt
```
## Uso

### Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/usuario/DiscreTool.git
```
    
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```
### Ejecución de Comandos

- **Operaciones comunes**:


- **Lógica Proposicional**:
```bash
python -m src.cli logic evaluate "A ∧ B → C" -a A True -a B False -a C True
```

- **Herramientas Comunes**:
```bash
python -m src.cli common_tools gcd 48 180
```

### Comandos Disponibles

- **logic evaluate**: Evalúa expresiones lógicas.
- **logic table**: Genera tablas de verdad.
- **common_tools gcd**: Calcula el MCD.
- **common_tools lcm**: Calcula el MCM.

## Contribuir

Si deseas contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios y haz commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Envía la rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un pull request.


## Estructura



## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

---
```
DiscreTool
├─ .gitignore
├─ examples
│  ├─ common_operations.md
│  └─ common_tools_examples.md
├─ README.md
├─ requirements.txt
├─ setup.py
├─ src
│  ├─ cli.py
│  ├─ combinatorics
│  │  ├─ combinatorics_cli.py
│  │  └─ combinatorics_solver.py
│  ├─ common_tools
│  │  ├─ common_tools_cli.py
│  │  ├─ congruences.py
│  │  ├─ gcd_lcm.py
│  │  ├─ modular_arithmetic.py
│  │  ├─ prime_factorization.py
│  │  ├─ prime_tools.py
│  │  └─ __init__.py
│  ├─ graphs
│  │  ├─ graphs_cli.py
│  │  └─ graph_algorithms.py
│  ├─ logic
│  │  ├─ complexity_analysis.py
│  │  ├─ derivation.py
│  │  ├─ equivalence_solver.py
│  │  ├─ inference.py
│  │  ├─ inference_rules.py
│  │  ├─ logic_cli.py
│  │  ├─ logic_solver.py
│  │  ├─ sat_solver.py
│  │  ├─ truth_table.py
│  │  └─ __init__.py
│  ├─ recursion
│  │  ├─ recursion_cli.py
│  │  └─ recursion_solver.py
│  ├─ utils
│  │  ├─ boolean_handler.py
│  │  ├─ error_handling.py
│  │  ├─ export_tools.py
│  │  ├─ expression_validator.py
│  │  ├─ helper.py
│  │  ├─ normalize_expression.py
│  │  ├─ visualize.py
│  │  └─ __init__.py
│  └─ __init__.py
├─ tasks.json
└─ tests
   ├─ test_cli.py
   ├─ test_common_tools.py
   └─ test_logic_solver.py

```