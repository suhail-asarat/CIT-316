import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue to store nodes with their f, g values and paths
    queue = [(0 + heuristic[start], 0, start, [start])]  # (f, g, node, path)
    visited = set()
    
    while queue:
        f, g, node, path = heapq.heappop(queue)
        
        if node in visited:
            continue
        visited.add(node)
        
        # If the goal is reached, return the cost and path
        if node == goal:
            return g, path
        
        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                new_g = g + cost
                f = new_g + heuristic.get(neighbor, float('inf'))
                heapq.heappush(queue, (f, new_g, neighbor, path + [neighbor]))
                
    return float("inf"), []

# Graph and heuristic values as given in the problem
graph = {
    'A': [('B', 2), ('E', 3)], 
    'B': [('A', 2), ('C', 1), ('G', 9)], 
    'C': [('B', 1)], 
    'D': [('E', 6), ('G', 1)], 
    'E': [('A', 3), ('D', 6)], 
    'G': [('B', 9), ('D', 1)]
}
heuristic = {
    'A': 11, 
    'B': 6, 
    'C': 99, 
    'D': 1, 
    'E': 7, 
    'G': 0  # heuristic for the goal node should be zero
}

# Execute A* from A to G
cost, path = a_star(graph, 'A', 'G', heuristic)
print("Cost-effective path:", path)
print("Total cost:", cost)
