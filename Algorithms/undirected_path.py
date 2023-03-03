def undirected_path(edges, node_A, node_B):
  graph = build_graph(edges)
  return hasPath(graph, node_A, node_B,visited = set())
  
def build_graph(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        if a not in graph: graph[a] = []; graph[a].append(b)
        else:
            graph[a].append(b)
        if b not in graph: graph[b] = []; graph[b].append(a)
        else:
            graph[b].append(a)
    return graph

def hasPath(graph, src, dst,visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for path in graph[src]:  
        if hasPath(graph, path, dst,visited) == True:
            return True
    return False