import heapq

def greedy_search(graph, start, goal, heuristic):
    queue = [(heuristic[start], start)]
    visited = set()
    
    while queue:
        _, node = heapq.heappop(queue)
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            return True
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (heuristic[neighbor], neighbor))
    return False

# Example usage
# graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
# heuristic = {'A': 5, 'B': 4, 'C': 6, 'D': 3, 'E': 2, 'F': 0}
# print(greedy_search(graph, 'A', 'F', heuristic))
