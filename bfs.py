from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
# graph = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
graph ={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A'],
    'D':['B','F'],
    'E':['B','G','H'],
    'F':['D'],
    'G':['E','I','J'],
    'H':['E','K'],
    'I':['G','L'],
    'J':['G','L'],
    'K':['H'],
    'L':['I','J']    
}
bfs(graph, 'A')
