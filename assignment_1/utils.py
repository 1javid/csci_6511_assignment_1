"""
Utility functions for the Water Pitchers Problem using A* search algorithm.
"""

__author__ = "Javid Alakbarli"
__credits__ = ["Javid Alakbarli"]
__version__ = "1.0.0"
__maintainer__ = "Javid Alakbarli"

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

def h_of_n(state, target, pitchers_capacity):
    """
    Heuristic function for A* search algorithm.
    
    Args:
        state (tuple): Current state of the pitchers.
        target (int): Target volume of water to be achieved.
        pitchers_capacity (list): List of capacities of the pitchers including the infinite pitcher.
    
    Returns:
        int: Heuristic estimate of the cost to reach the goal from the current state.
    """
    current = state[-1]  # Water in infinite pitcher
    remaining = target - current
    if remaining == 0:
        return 0
    
    max_pitcher = max(pitchers_capacity[:-1])  
    return math.ceil(abs(remaining) / max_pitcher)


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