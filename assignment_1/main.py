from utils import *

def a_star_pitchers():
    """
    Implements A* search algorithm to solve the Water Pitchers Problem.
    
    The problem:
    - Given n pitchers with different capacities (last one being infinite)
    - Find minimum number of steps to get target amount in infinite pitcher
    - Operations allowed: fill pitcher, pour from one pitcher to another
    
    Returns:
        int: Minimum number of steps to reach target, or -1 if no solution exists
    """
    pitchers_capacity, target = read_input()

    # Find largest finite pitcher capacity for heuristic calculation
    max_capacity = max(pitchers_capacity[:-1])

    # Early termination if target is not achievable
    if not is_solvable(pitchers_capacity, target):
        return -1   # Target not achievable with given pitcher capacities

    # Initialize starting state where all pitchers are empty
    pitchers_0 = tuple([0] * len(pitchers_capacity))
    g_0 = 0  # Initial cost (steps taken) is 0
    h_0 = h_of_n(pitchers_0, target, max_capacity)  # Initial heuristic estimate
    f_0 = f_of_n(g_0, h_0)  # Initial total cost estimate (f = g + h)

    # Priority queue for A* search - stores (f_value, g_value, state)
    priority_queue = []
    push(priority_queue, (f_0, g_0, pitchers_0))

    # Keep track of visited states and their costs to avoid cycles
    visited = {pitchers_0: g_0}
    n = len(pitchers_capacity)

    while priority_queue:
        f, g, state = pop(priority_queue)  # Get state with lowest f-value

        # Goal test: check if target amount is in infinite pitcher
        if state[-1] == target:
            return g  # Return number of steps taken

        # Generate successor states through valid operations
        expanded_nodes = []
        # Try filling each pitcher
        for new_state in fill_pitchers(state, pitchers_capacity, n):
            expanded_nodes.append(new_state)
        # Try pouring between each pair of pitchers
        for new_state in pour_between_pitchers(state, pitchers_capacity, n, target):
            expanded_nodes.append(new_state)

        # Process each successor state
        for new_state in expanded_nodes:
            if new_state in visited:
                continue  # Skip already visited states
            new_g = g + 1  # Increment step count
            new_h = h_of_n(new_state, target, max_capacity)  # Calculate new heuristic
            new_f = f_of_n(new_g, new_h)  # Calculate new total cost
            push(priority_queue, (new_f, new_g, new_state))
            visited[new_state] = new_g  # Mark state as visited

    return -1  # No solution found after exploring all possible states

if __name__ == "__main__":
    result = a_star_pitchers()
    if result != -1:
        print("Number of steps:", result)
    else:
        print("No solution found")