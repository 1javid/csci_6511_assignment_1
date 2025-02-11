# Water Pitchers Problem using A* Algorithm

This project implements a solution to the Water Pitchers Problem using the A* search algorithm. The problem involves manipulating water between pitchers of different capacities to achieve a target volume in one of the pitchers.

## Problem Description

Given:
- A set of pitchers with different capacities
- An infinite water source
- A target volume

Goal: Find the minimum number of steps required to measure the target volume using the given pitchers.

## Implementation

The solution uses the following components:

- [`main.py`](assignment_1/main.py): Contains the A* algorithm implementation
- [`utils.py`](assignment_1/utils.py): Helper functions for:
  - Reading input
  - Heuristic calculation
  - State expansion
  - Priority queue operations
- [`unit_tests.py`](assignment_1/unit_tests.py): Comprehensive test cases

## Input Format

The input file (`input.txt`) should contain:

```sh
pitcher1_capacity,pitcher2_capacity,pitcher3_capacity,... 
target_volume
```

Example:

```sh
2,3,5
4
```

## Running the Program

```bash
pyhton main.py
```

The program will output either:
- **"Number of steps: X** where X is the minimum steps required
- **"No solution found"** if the target is impossible to achieve

## Testing

Run the unit tests with:

```bash
python -m unittest unit_tests.py
```

## Algorithm Details

The implementation uses:

- A* search with an admissible heuristic
- Priority queue for the open list
- Dictionary for the closed list (visited states)
- State generation through filling and pouring operations