def hasPath(graph, src, dst):
    if src == dst:
        return True
    for path in graph[src]:
       if hasPath(graph, path, dst) == True:
           return True
    return False
         
         
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': [] 
  }

hasPath(graph, 'f', 'k')