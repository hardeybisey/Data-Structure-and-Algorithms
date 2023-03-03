def largest_component(graph):
    visited = set()
    largest = 0
    for component in graph:
        size = traverse(graph, component,visited)
        if size > largest:  largest = size
    return largest   
    
def traverse(graph, node, visited):
    if node in visited: return 0
    visited.add(node)
    size = 1
    for neighbor in graph[node]:
        size+= traverse(graph, neighbor, visited)
    return size