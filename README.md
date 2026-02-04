# 2-Strong Roman Domination Project

## Overview

This repository contains the implementation of heuristic and meta-heuristic algorithms for the 2-Strong Roman Domination problem, including a Genetic Algorithm (GA) and a Biased Random-Key Genetic Algorithm (BRKGA). The complete work, including the problem motivation, mathematical modeling, and experimental results, is documented in the final report `tcc_lucas.pdf`, available in the root of this repository.

## Repository Structure

- `main/`: Main project source code, tools, and scripts.
  - `src/`: Algorithm implementations (GA, BRKGA), utilities, and converters.
  - `src/irace_tunning/`: Files for parameter tuning with the IRACE package (parameters, scenario, and runner script).
- `tcc_lucas.pdf`: The final thesis report detailing the problem and experiments.
- `pyproject.toml`: Project metadata and Python dependencies.
- `main.py`: (entry point, where applicable)
- **Test Graphs**: The graph instances used for the experiments are available on [Google Drive](https://drive.google.com/drive/folders/1gRFxtc8M5AIJg5Xeq-AQw8R2ZhM-xPU0?hl=pt-br).

## Dependencies

This project requires Python 3.12+ and the libraries listed in `pyproject.toml`. Key dependencies include:

- networkx
- numpy
- pymoo
- scipy
- geopandas (used in specific parts)
- cplex / docplex / ortools (optional, used for experiments that rely on these solvers)

## Recommended Installation

1.  Create and activate a virtual environment with uv.

    ```bash
    uv venv
    source .venv/bin/activate
    ```

2.  Install the dependencies. You can install them from the `pyproject.toml` if you have a modern package manager, or install them manually.


## Usage

Below are examples of how to run the main algorithm scripts from the command line.

1.  **Genetic Algorithm (GA):**

    ```bash
    python3 main/src/ga.py \
      --instance path/to/instance.txt \
      --population_size 100 \
      --gene_mutation_rate 0.1 \
      --n_mutants 0.2 \
      --crossover_rate 0.7 \
      --seed 1
    ```

2.  **Biased Random-Key Genetic Algorithm (BRKGA):**

    ```bash
    python3 main/src/brkga.py \
      --instance path/to/instance.txt \
      --n_elites 20 \
      --n_offsprings 50 \
      --n_mutants_brkga 10 \
      --bias 0.7 \
      --population_size 100 \
      --seed 1
    ```

### Parameter Tuning with IRACE

The `main/src/irace_tunning/` directory contains `target-runner.py`, `parameters.txt`, and `scenario.txt` for use with the R package `irace`. To run the tuning process, you need R and the `irace` package installed.


## Utilities

-   **Graph Format Conversion**: The `main/src/scripts/filter_graphs/` directory contains scripts to convert graph instances from Matrix Market (.mtx) to the edge list format used by the algorithms.
-   **CLI Scripts**: The command-line interface scripts (e.g., `run_ga_cli.py`) are designed to output the objective function value (cost) to stdout, allowing for easy integration with IRACE.

## Results and Report

For a complete description of the problem, methodology, and experimental results, please refer to `tcc_lucas.pdf`. The report includes tables, charts, and analysis of the implemented methods' performance.

## Contributing

If you wish to contribute, please open an issue describing the proposed change or submit a pull request with minimal tests and documentation for the changes.



## License

This repository does not currently contain an explicit license file.
