import random

def hill_climbing(problem):
    current = problem.initial_state()
    while True:
        neighbors = problem.get_neighbors(current)
        if not neighbors:
            break
        neighbor = max(neighbors, key=problem.value)
        if problem.value(neighbor) <= problem.value(current):
            break
        current = neighbor
    return current

# Define problem for testing
class SimpleProblem:
    def initial_state(self):
        return random.randint(0, 100)
    
    def get_neighbors(self, state):
        return [state - 1, state + 1]
    
    def value(self, state):
        return -((state - 50) ** 2) + 100  # Peak at 50 for demonstration

# Example usage
problem = SimpleProblem()
print("Best state:", hill_climbing(problem))
