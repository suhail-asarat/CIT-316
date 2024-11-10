def dls(graph, start, goal, limit):
    if start == goal:
        return True
    if limit <= 0:
        return False
    
    for neighbor in graph[start]:
        if dls(graph, neighbor, goal, limit - 1):
            return True
    return False

# Example usage
# graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
# print(dls(graph, 'A', 'F', 2))
