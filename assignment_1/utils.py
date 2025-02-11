import heapq
import math

def read_input():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        pitchers_capacity = [int(x) for x in lines[0].split(',')]
        
        pitchers_capacity.append(float('inf'))
        target = int(lines[1])
        
        return pitchers_capacity, target

def h_of_n(state, target):
    return max(0, target - state[-1])

def g_of_n(g):
    return g + 1

def f_of_n(g, h):
    return g + h

def fill_pitchers(state, pitchers_capacity, n):
    """Fill empty or partially filled pitchers to their capacity"""
    expanded_nodes = []
    for i in range(n - 1):  # Exclude infinite pitcher
        if state[i] < pitchers_capacity[i]:
            pitchers_next = list(state)
            pitchers_next[i] = pitchers_capacity[i]
            expanded_nodes.append(tuple(pitchers_next))
    return expanded_nodes

def pour_between_pitchers(state, pitchers_capacity, n, target):
    """Pour water between pitchers including infinite pitcher"""
    expanded_nodes = []
    for i in range(n):
        if state[i] == 0:
            continue

        for j in range(n):
            if i == j or (j != n - 1 and state[j] == pitchers_capacity[j]):
                continue

            available = pitchers_capacity[j] - state[j] if j != n - 1 else None

            if i != n - 1:  # Pouring from finite pitcher
                if j == n - 1:
                    pour = state[i]
                else:
                    pour = min(state[i], available)
                
                new_state = list(state)
                new_state[i] -= pour
                new_state[j] += pour
                expanded_nodes.append(tuple(new_state))
            else:  # Pouring from infinite pitcher
                pour_needed = state[i] - target
                if pour_needed < 0:
                    continue
                max_pour = min(pour_needed, available)
                new_state = list(state)
                new_state[i] -= max_pour
                new_state[j] += max_pour
                expanded_nodes.append(tuple(new_state))
    return expanded_nodes

def push(queue, item):
    heapq.heappush(queue, item)

def pop(queue):
    return heapq.heappop(queue)