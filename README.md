# DiscreTool

**DiscreTool** es una herramienta de línea de comandos (CLI) desarrollada en Python, diseñada para ayudar a resolver problemas comunes en Matemáticas Discretas. Esta herramienta incluye funcionalidades para trabajar con lógica proposicional, operaciones comunes como el cálculo del máximo común divisor (MCD), mínimo común múltiplo (MCM), congruencias y mucho más.

## Características

### Lógica Proposicional

- **Evaluación de expresiones lógicas**: Evalúa expresiones con asignaciones de verdad a variables proposicionales.
- **Generación de tablas de verdad**: Genera tablas de verdad para cualquier expresión lógica.
- **Simplificación**: Simplifica expresiones lógicas en formas normales disyuntivas (DNF) y conjuntivas (CNF).
- **Equivalencia**: Verifica si dos expresiones lógicas son equivalentes.
- **Clasificación**: Clasifica expresiones como tautologías, contradicciones o contingencias.
- **Deducción natural**: Aplica reglas de inferencia (como Modus Ponens y Silogismo Disyuntivo) para derivar conclusiones.

### Herramientas Comunes de Matemáticas Discretas

- **Cálculo del MCD (Máximo Común Divisor)**.
- **Cálculo del MCM (Mínimo Común Múltiplo)**.
- **Generación de números primos**: Genera todos los números primos hasta un valor dado.
- **Congruencias**: Verifica si dos números son congruentes bajo un módulo dado.
- **Resolución de ecuaciones diofánticas**: Resuelve ecuaciones del tipo ax+by=cax + by = cax+by=c.

A futuro: 
- mathcli combinatorics: Combinaciones y permutaciones.
- mathcli graphs: Operaciones sobre grafos.
- mathcli recursion: Algoritmos recursivos.
## Requisitos

Para ejecutar DiscreTool, necesitas tener instalados los siguientes paquetes de Python:

- Python 3.x
- `Click`
- `SymPy`
- `PySAT` 

Puedes instalar las dependencias ejecutando:

`pip install -r requirements.txt`

## Uso

### Instalación

1. Clona este repositorio:
    
```bash
git clone https://github.com/usuario/DiscreTool.git
```
    
2. Instala las dependencias:
    
```bash
pip install -r requirements.txt
```
### Ejecución

### Comandos Disponibles

## Contribuir

Si quieres contribuir al desarrollo de **DiscreTool**, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Envía tu rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un pull request.

## Licencia

Este proyecto está licenciado bajo la licencia MIT - mira el archivo LICENSE para más detalles.


```
DiscreTool
├─ .git
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ setup.py
├─ src
│  ├─ cli.py
│  ├─ combinatorics
│  │  └─ combinatorics_solver.py
│  ├─ common_tools
│  │  ├─ congruences.py
│  │  ├─ gcd_lcm.py
│  │  ├─ prime_tools.py
│  │  └─ __init__.py
│  ├─ graphs
│  │  └─ graph_algorithms.py
│  ├─ logic
│  │  ├─ derivation.py
│  │  ├─ inference.py
│  │  ├─ logic_solver.py
│  │  ├─ sat_solver.py
│  │  └─ __init__.py
│  ├─ utils
│  │  ├─ helper.py
│  │  ├─ replace_implication.py
│  │  └─ __init__.py
│  └─ __init__.py
├─ tasks.json
└─ tests
   └─ test_logic_solver.py

```