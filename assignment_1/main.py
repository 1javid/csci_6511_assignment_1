"""
A* search algorithm to solve the Water Pitchers Problem.
"""

__author__ = "Javid Alakbarli"
__credits__ = ["Javid Alakbarli"]
__version__ = "1.1.0"
__maintainer__ = "Javid Alakbarli"

from utils import *

def a_star_pitchers():
    """
    The problem:
    - Given n pitchers with different capacities (last one being infinite)
    - Find minimum number of steps to get target amount in infinite pitcher
    - Operations allowed: fill pitcher, pour from one pitcher to another

    Returns:
        tuple: (steps, moves) Minimum number of steps to reach target and list of moves taken, 
               or -1 if no solution exists
    """
    pitchers_capacity, target = read_input()

    # Early termination if target is not achievable
    if not is_solvable(pitchers_capacity, target):
        return -1   # Target not achievable with given pitcher capacities

    # Initialize starting state where all pitchers are empty
    initial_state = tuple([0] * len(pitchers_capacity))
    initial_path = []  # No moves made yet
    g_0 = 0  # Initial cost (steps taken) is 0
    h_0 = h_of_n(initial_state, target, pitchers_capacity)  
    f_0 = f_of_n(g_0, h_0)  

    # Priority queue for A* search - stores tuples: (f_value, g_value, state, path)
    priority_queue = []
    push(priority_queue, (f_0, g_0, initial_state, initial_path))

    # Keep track of visited states to avoid cycles
    visited = set([initial_state])
    n = len(pitchers_capacity)

    while priority_queue:
        f, g, state, path = pop(priority_queue)  # Get state with lowest f-value

        # Goal test: check if target amount is in the infinite pitcher (assumed to be the last one)
        if state[-1] == target:
            return (g, path)  # Return number of steps taken and the moves path

        expanded_nodes = []
        # Generate filling moves (only for pitchers with finite capacity, i.e. all but the infinite pitcher)
        for i in range(n - 1):
            if state[i] < pitchers_capacity[i]:
                new_state = list(state)
                new_state[i] = pitchers_capacity[i]
                new_state = tuple(new_state)
                move_desc = f"Fill pitcher {i} to {pitchers_capacity[i]}"
                expanded_nodes.append((new_state, move_desc))
        # Generate pouring moves for all pairs of pitchers (i -> j)
        for i in range(n):
            if state[i] == 0:
                continue  # Nothing to pour from pitcher i
            for j in range(n):
                if i == j:
                    continue
                cap_j = pitchers_capacity[j]
                if cap_j != float('inf'):
                    if state[j] < cap_j:
                        amount = min(state[i], cap_j - state[j])
                        new_state = list(state)
                        new_state[i] -= amount
                        new_state[j] += amount
                        new_state = tuple(new_state)
                        move_desc = f"Pour {amount} from pitcher {i} to pitcher {j}"
                        expanded_nodes.append((new_state, move_desc))
                else:
                    # For the infinite pitcher, pour all water from pitcher i
                    if state[i] > 0:
                        amount = state[i]
                        new_state = list(state)
                        new_state[i] = 0
                        new_state[j] = state[j] + amount
                        new_state = tuple(new_state)
                        move_desc = f"Pour {amount} from pitcher {i} to infinite pitcher {j}"
                        expanded_nodes.append((new_state, move_desc))

        # Process each successor state
        for new_state, move_desc in expanded_nodes:
            if new_state in visited:
                continue  # Skip already visited states
            
            new_g = g + 1
            new_h = h_of_n(new_state, target, pitchers_capacity)
            new_f = f_of_n(new_g, new_h)
            new_path = path + [move_desc]
            push(priority_queue, (new_f, new_g, new_state, new_path))
            visited.add(new_state)

    return -1  # No solution found after exploring all possible states

if __name__ == "__main__":
    result = a_star_pitchers()
    if result != -1:
        steps, moves = result
        print("Number of steps:", steps)
        print("Moves taken:")
        for move in moves:
            print(move)
    else:
        print("No solution found")