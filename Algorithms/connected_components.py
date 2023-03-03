def connected_components_count(graph):
    visited = set()
    count = 0
    for component in graph:
        print(visited)
        if traverse(graph, component,visited) == True: count+=1
    return count   
    
def traverse(graph, node, visited):
    if node in visited: return False
    visited.add(node)
    for neighbor in graph[node]:
        traverse(graph, neighbor, visited)
    return True