# Polynomial function Genetic Algorithm

This is a simple genetic algorithm designed to find the maximum of a second degree polynomial function. It consists of a core library written in C,
a Ctypes python wrapper and an algorithm written in python.

## Features and techonology

- *Core functions:* A C implementation of roulette-wheel selection intervals, binary encoding/decoding, bit-level crossover, and mutation. 
- *Execution and visualisation:* The `Ctypes` wrapper and algorithm are written in python, with a visualisation using `matplotlib`.
- *Configuration:* The tweak population sizes, domain boundaries, polynomial coefficients, precision, and mutation/crossover probabilities can be changed via the configuration file.

## Structure

- `genetic.h` / `genetic.c`: The core C library. 
- `genetic.py`: Python wrapper utilizing `ctypes`.
- `algorithm.py`: The main execution script. 
- `parameters.in`: Configuration file for algorithm parameters.

## Compilation and execution

1. Compilte the library: 
```
    gcc -c -Wall -Werror -fpic genetic.c
    gcc -shared -o genetic.so libgenetic.o
```
2. Add the library to the path: 
```
    sudo cp ./libgenetic.so /usr/lib
    chmod 777 /usr/lib/libgenetic.so
    ldconfig
```
3. Configure parameters.in
4. Run with python3 algortihm.py

## Parameter configuration

The file format expects:

- Chromosome count (population size)
- Domain boundaries (min max)
- Polynomial coefficients ($a, b, c$ for $ax^2 + bx + c$)
- Precision (number of decimal places)
- Crossover probability (e.g., 0.25)
- Mutation probability (e.g., 0.01)
- Number of generations/steps (e.g., 50)

## Licence

Distributed under GPL3
