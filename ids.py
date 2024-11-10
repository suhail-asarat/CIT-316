def ids(graph, start, goal, max_depth):
    def dls(node, depth):
        if depth == 0 and node == goal:
            return True
        if depth > 0:
            for neighbor in graph[node]:
                if dls(neighbor, depth - 1):
                    return True
        return False
    
    for depth in range(max_depth):
        if dls(start, depth):
            return True
    return False

# Example usage
# graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
# print(ids(graph, 'A', 'F', 3))
