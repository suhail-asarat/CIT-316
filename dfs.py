def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

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
dfs(graph, 'A')
