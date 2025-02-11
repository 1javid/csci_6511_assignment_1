from utils import *

def a_star_pitchers():
    pitchers_capacity, target = read_input()
    pitchers_0 = tuple([0] * len(pitchers_capacity))

    g_0 = 0
    h_0 = h_of_n(pitchers_0, target)
    f_0 = f_of_n(g_0, h_0)

    priority_queue = []  # open list
    push(priority_queue, (f_0, g_0, pitchers_0))

    visited = {pitchers_0: g_0}  # closed list
    n = len(pitchers_capacity)

    while priority_queue:
        f, g, state = pop(priority_queue)
        infinite_pitcher = state[-1]

        if infinite_pitcher == target:
            return g
        
        # Generate successor states
        expanded_nodes = fill_pitchers(state, pitchers_capacity, n)
        expanded_nodes.extend(pour_between_pitchers(state, pitchers_capacity, n, target))
        
        # Process expanded nodes
        for neighbor in expanded_nodes:
            if neighbor in visited:
                continue

            new_g = g + 1
            new_h = h_of_n(neighbor, target)
            new_f = f_of_n(new_g, new_h)
            push(priority_queue, (new_f, new_g, neighbor))
            visited[neighbor] = new_g

    return -1

if __name__ == "__main__":
    result = a_star_pitchers()
    if result != -1:
        print("Number of steps:", result)
    else:
        print("No solution found")