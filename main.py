import bfs
import dfs
import ucs
import ids
import dls
import bidirectional_search
import greedy_search
import a_star
import hill_climbing
import genetic_algorithm
import constraint_satisfaction
import arc_consistency
import sudoku_solver
import bayesian_network
import decision_tree
import linear_regression
import basic_perceptron
import neural_network

def main():
    print("Choose an algorithm to run:")
    algorithms = [
        "1. Breadth-First Search (BFS)",
        "2. Depth-First Search (DFS)",
        "3. Uniform Cost Search (UCS)",
        "4. Iterative Deepening Search (IDS)",
        "5. Depth-Limited Search (DLS)",
        "6. Bidirectional Search",
        "7. Greedy Search",
        "8. A* Search",
        "9. Hill Climbing",
        "10. Genetic Algorithm",
        "11. Constraint Satisfaction Problem",
        "12. Arc Consistency",
        "13. Sudoku Solver",
        "14. Bayesian Network",
        "15. Decision Tree",
        "16. Linear Regression",
        "17. Basic Perceptron",
        "18. Neural Network"
    ]
    for alg in algorithms:
        print(alg)
    
    choice = input("Enter the number of the algorithm you want to run: ")
    
    if choice == '1':
        graph = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
        bfs.bfs(graph, 'A')
    elif choice == '2':
        graph = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
        dfs.dfs(graph, 'A')
    elif choice == '3':
        graph = {'A': [('B', 1), ('C', 2)], 'B': [('A', 1), ('D', 3), ('E', 1)], 'C': [('A', 2), ('F', 4)], 'D': [('B', 3)], 'E': [('B', 1), ('F', 5)], 'F': [('C', 4), ('E', 5)]}
        print(ucs.ucs(graph, 'A', 'F'))
    elif choice == '4':
        graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
        print(ids.ids(graph, 'A', 'F', 3))
    elif choice == '5':
        graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
        print(dls.dls(graph, 'A', 'F', 2))
    elif choice == '6':
        graph = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
        print(bidirectional_search.bidirectional_search(graph, 'A', 'F'))
    elif choice == '7':
        graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
        heuristic = {'A': 5, 'B': 4, 'C': 6, 'D': 3, 'E': 2, 'F': 0}
        print(greedy_search.greedy_search(graph, 'A', 'F', heuristic))
    elif choice == '8':
        graph = {'A': [('B', 1), ('C', 2)], 'B': [('A', 1), ('D', 3), ('E', 1)], 'C': [('A', 2), ('F', 4)], 'D': [('B', 3)], 'E': [('B', 1), ('F', 5)], 'F': [('C', 4), ('E', 5)]}
        heuristic = {'A': 5, 'B': 4, 'C': 6, 'D': 3, 'E': 2, 'F': 0}
        print(a_star.a_star(graph, 'A', 'F', heuristic))
    elif choice == '9':
        problem = hill_climbing.SimpleProblem()
        print("Best state:", hill_climbing.hill_climbing(problem))
    elif choice == '10':
        population = [[random.randint(0, 1) for _ in range(10)] for _ in range(20)]
        best = genetic_algorithm.genetic_algorithm(population, genetic_algorithm.fitness, genetic_algorithm.mutate, genetic_algorithm.crossover)
        print("Best individual:", best)
    elif choice == '11':
        variables = ['A', 'B', 'C']
        domains = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}
        constraints = [lambda var, value, assignment: all(value != assignment.get(other) for other in assignment)]
        solution = constraint_satisfaction.constraint_satisfaction(variables, domains, constraints)
        print("Solution:", solution)
    elif choice == '12':
        csp = arc_consistency.SimpleCSP()
        arc_consistent = arc_consistency.arc_consistency(csp)
        print("Arc Consistent:", arc_consistent)
        print("Domains after AC-3:", csp.domains)
    elif choice == '13':
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            # Add the rest of the board for testing
        ]
        sudoku_solver.sudoku_solver(board)
        print("Solved Board:", board)
    elif choice == '14':
        bn = bayesian_network.BayesianNetwork()
        bn.add_variable('Rain', {True: 0.2, False: 0.8})
        print("P(Rain=True):", bn.get_probability('Rain', {}))
    elif choice == '15':
        X = [[0, 0], [1, 1]]
        y = [0, 1]
        model = decision_tree.decision_tree_train(X, y)
        print("Predicted:", model.predict([[2, 2]]))
    elif choice == '16':
        X = [[0], [1], [2], [3]]
        y = [0, 1, 2, 3]
        model = linear_regression.linear_regression_train(X, y)
        print("Predicted:", model.predict([[4]]))
    elif choice == '17':
        X = [[1, 1], [2, 2], [3, 3]]
        y = [0, 1, 1]
        p = basic_perceptron.Perceptron()
        p.fit(X, y)
        predictions = p.predict(X)
        print("Predictions:", predictions)
    elif choice == '18':
        X = [[0, 0], [1, 1]]
        y = [0, 1]
        model = neural_network.neural_network_train(X, y)
        print("Predicted:", model.predict([[2, 2]]))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
