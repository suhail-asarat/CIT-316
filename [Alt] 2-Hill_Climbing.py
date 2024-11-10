import copy

# Define the puzzle problem for hill climbing
class SlidePuzzleProblem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def initial_state(self):
        return self.initial

    def is_goal(self, state):
        return state == self.goal

    # Get all possible neighbors (moves)
    def get_neighbors(self, state):
        neighbors = []
        blank_pos = [(row_i, col_i) for row_i, row in enumerate(state) for col_i, val in enumerate(row) if val == 0][0]

        # Possible moves: up, down, left, right
        directions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

        for move, (dr, dc) in directions.items():
            new_r, new_c = blank_pos[0] + dr, blank_pos[1] + dc
            if 0 <= new_r < 3 and 0 <= new_c < 3:
                new_state = copy.deepcopy(state)
                # Swap blank (0) with the target tile
                new_state[blank_pos[0]][blank_pos[1]], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[blank_pos[0]][blank_pos[1]]
                neighbors.append(new_state)

        return neighbors

    # Heuristic function based on Manhattan distance
    def value(self, state):
        distance = 0
        for row in range(3):
            for col in range(3):
                val = state[row][col]
                if val != 0:
                    # Goal position of the tile with value `val`
                    goal_row, goal_col = (val - 1) // 3, (val - 1) % 3
                    # Manhattan distance from current position to goal position
                    distance += abs(row - goal_row) + abs(col - goal_col)
        return -distance  # More negative distance means worse state

# Hill-Climbing search algorithm
def hill_climbing(problem):
    current = problem.initial_state()
    while True:
        neighbors = problem.get_neighbors(current)
        if not neighbors:
            break
        # Select the neighbor with the lowest Manhattan distance
        neighbor = max(neighbors, key=problem.value)
        if problem.value(neighbor) <= problem.value(current):
            break  # Stop if no better neighbor is found
        current = neighbor
        print("Current state:", current)
    return current

# Define initial and goal states for the puzzle
initial_state = [
    [3, 8, 5],
    [0, 7, 1],
    [2, 6, 4]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Create the problem instance and solve it
problem = SlidePuzzleProblem(initial_state, goal_state)
solution = hill_climbing(problem)
print("Final state:", solution)
