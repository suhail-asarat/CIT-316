def arc_consistency(csp):
    queue = [(x, y) for x in csp.variables for y in csp.constraints[x]]
    
    while queue:
        (x, y) = queue.pop(0)
        if revise(csp, x, y):
            if not csp.domains[x]:
                return False
            for z in csp.constraints[x]:
                if z != y:
                    queue.append((z, x))
    return True

def revise(csp, x, y):
    revised = False
    for x_val in csp.domains[x]:
        if all(not csp.is_consistent(x_val, y_val) for y_val in csp.domains[y]):
            csp.domains[x].remove(x_val)
            revised = True
    return revised

# Define a sample CSP class for testing
class SimpleCSP:
    def __init__(self):
        self.variables = ['A', 'B']
        self.domains = {'A': [1, 2, 3], 'B': [2, 3]}
        self.constraints = {'A': ['B'], 'B': ['A']}

    def is_consistent(self, x_val, y_val):
        return x_val != y_val

# Example usage
# csp = SimpleCSP()
# arc_consistent = arc_consistency(csp)
# print("Arc Consistent:", arc_consistent)
# print("Domains after AC-3:", csp.domains)
