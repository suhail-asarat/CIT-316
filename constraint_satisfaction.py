def constraint_satisfaction(variables, domains, constraints):
    assignment = {}

    def backtrack(assignment):
        if len(assignment) == len(variables):
            return assignment
        var = select_unassigned_variable(variables, assignment)
        for value in domains[var]:
            if is_consistent(var, value, assignment, constraints):
                assignment[var] = value
                result = backtrack(assignment)
                if result:
                    return result
                del assignment[var]
        return None

    return backtrack(assignment)

def select_unassigned_variable(variables, assignment):
    for var in variables:
        if var not in assignment:
            return var

def is_consistent(var, value, assignment, constraints):
    for constraint in constraints:
        if not constraint(var, value, assignment):
            return False
    return True

# Example usage
# variables = ['A', 'B', 'C']
# domains = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}
# constraints = [
#     lambda var, value, assignment: all(value != assignment.get(other) for other in assignment)
# ]
# solution = constraint_satisfaction(variables, domains, constraints)
# print("Solution:", solution)
