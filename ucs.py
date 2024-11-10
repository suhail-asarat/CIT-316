import heapq

def ucs(graph, start, goal):
    queue = [(0, start)]
    visited = set()
    
    while queue:
        cost, node = heapq.heappop(queue)
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            return cost
        
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor))

# Example usage
# graph = {'A': [('B', 1), ('C', 2)], 'B': [('A', 1), ('D', 3), ('E', 1)], 'C': [('A', 2), ('F', 4)], 'D': [('B', 3)], 'E': [('B', 1), ('F', 5)], 'F': [('C', 4), ('E', 5)]}
# print(ucs(graph, 'A', 'F'))
