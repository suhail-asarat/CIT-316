from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return True
    
    start_visited, goal_visited = {start}, {goal}
    start_queue, goal_queue = deque([start]), deque([goal])
    
    while start_queue and goal_queue:
        if start_queue:
            node = start_queue.popleft()
            if node in goal_visited:
                return True
            for neighbor in graph[node]:
                if neighbor not in start_visited:
                    start_visited.add(neighbor)
                    start_queue.append(neighbor)
        
        if goal_queue:
            node = goal_queue.popleft()
            if node in start_visited:
                return True
            for neighbor in graph[node]:
                if neighbor not in goal_visited:
                    goal_visited.add(neighbor)
                    goal_queue.append(neighbor)
    return False

# Example usage
# graph = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
# print(bidirectional_search(graph, 'A', 'F'))
