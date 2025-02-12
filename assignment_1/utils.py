import heapq
import math

def read_input():
    """
    Reads problem input from input.txt file.
    
    Returns:
        tuple: (list of pitcher capacities with infinite pitcher appended, target volume)
    """
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        pitchers_capacity = [int(x) for x in lines[0].split(',')]
        pitchers_capacity.append(float('inf'))  # Add infinite pitcher
        target = int(lines[1])
        return pitchers_capacity, target

def h_of_n(state, target, max_capacity):
    """
    Heuristic function for A* search.
    Estimates minimum steps needed to reach target from current state.
    
    Args:
        state: Current state (tuple of water levels in each pitcher)
        target: Target water amount
        max_capacity: Capacity of largest finite pitcher
    
    Returns:
        int: Estimated minimum steps to reach target
    """
    current = state[-1]  # Amount in infinite pitcher
    remaining = target - current
    if remaining <= 0: 
        return 0
    return math.ceil(remaining / max_capacity)

def f_of_n(g, h):
    """
    Calculates f-value for A* search (f = g + h).
    
    Args:
        g: Cost so far (steps taken)
        h: Heuristic estimate to goal
    
    Returns:
        int: Total estimated cost
    """
    return g + h

def fill_pitchers(state, pitchers_capacity, n):
    """
    For each finite pitcher (i.e. all but the infinite pitcher), if it is not full,
    produce a new state where the pitcher is filled.
    Returns a tuple: new_state.
    """
    expanded_nodes = []
    for i in range(n - 1):  # Exclude the infinite pitcher.
        if state[i] < pitchers_capacity[i]:
            new_state = list(state)
            new_state[i] = pitchers_capacity[i]
            expanded_nodes.append(tuple(new_state))
    return expanded_nodes

def pour_between_pitchers(state, pitchers_capacity, n, target):
    """
    For each pair of pitchers (source and destination), if a valid pour exists,
    pour water so that either the source becomes empty or the destination is full.
    Returns a tuple: new_state.
    """
    expanded_nodes = []
    for i in range(n):  # Source pitcher.
        if state[i] == 0:
            continue  # Nothing to pour from an empty pitcher.
        for j in range(n):  # Destination pitcher.
            if i == j or state[j] == pitchers_capacity[j]:
                continue  # Skip if same pitcher or destination is already full.
            available_space = pitchers_capacity[j] - state[j]
            pour_amount = min(state[i], available_space)
            if pour_amount > 0:
                new_state = list(state)
                new_state[i] -= pour_amount
                new_state[j] += pour_amount
                expanded_nodes.append(tuple(new_state))
    return expanded_nodes

def push(queue, item):
    heapq.heappush(queue, item)

def pop(queue):
    return heapq.heappop(queue)

def is_solvable(pitchers_capacity, target):
    """
    Check if the target is achievable using the finite pitchers' capacities.
    Since the last pitcher is infinite, it is excluded from the GCD calculation.
    """
    finite_pitchers = pitchers_capacity[:-1]  # Exclude the infinite pitcher.
    gcd_value = math.gcd(*finite_pitchers)
    return target % gcd_value == 0