import heapq

def a_star(graph, start, goal, heuristic):
    queue = [(0 + heuristic[start], 0, start)]
    visited = set()
    
    while queue:
        f, g, node = heapq.heappop(queue)
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            return g
        
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                f = new_g + heuristic[neighbor]
                heapq.heappush(queue, (f, new_g, neighbor))
    return float("inf")

# Example usage
# graph = {'A': [('B', 1), ('C', 2)], 'B': [('A', 1), ('D', 3), ('E', 1)], 'C': [('A', 2), ('F', 4)], 'D': [('B', 3)], 'E': [('B', 1), ('F', 5)], 'F': [('C', 4), ('E', 5)]}
# heuristic = {'A': 5, 'B': 4, 'C': 6, 'D': 3, 'E': 2, 'F': 0}
# print(a_star(graph, 'A', 'F', heuristic))
