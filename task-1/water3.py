def initial_state():
    return (0, 0, 0)

def is_goal(s):
    a, b, c = s
    return a == 4 and b == 4

def successors(s):
    x, y, z = s
    successor_states = []

    pour_actions = [
        (0, 1),  # Pour from 8-liter to 5-liter
        (0, 2),  # Pour from 8-liter to 3-liter
        (1, 0),  # Pour from 5-liter to 8-liter
        (1, 2),  # Pour from 5-liter to 3-liter
        (2, 0),  # Pour from 3-liter to 8-liter
        (2, 1),  # Pour from 3-liter to 5-liter
    ]
    
    for pour in pour_actions:
        source, destination = pour
        if s[source] > 0 and s[destination] < 5:
            # Calculate the amount to pour
            amount_to_pour = min(s[source], 5 - s[destination])
            # Create a new state by pouring water
            new_state = list(s)
            new_state[source] -= amount_to_pour
            new_state[destination] += amount_to_pour
            successor_states.append(tuple(new_state))
            
    return successor_states
