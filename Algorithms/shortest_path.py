def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)
  queue = [(node_A,0)]
  visited = set()
  while queue:
    node , distance = queue.pop(0)
    if node == node_B:
      return distance
    
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor,distance+1))
  return -1

def build_graph(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        if a not in graph:  graph[a] = []; graph[a].append(b)
        else:
            graph[a].append(b)
        if b not in graph: graph[b] = []; graph[b].append(a)
        else: 
            graph[b].append(a)
    return graph