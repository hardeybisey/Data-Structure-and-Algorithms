def minimum_island(grid):
    visited = set()
    min_size =  float('inf')
    for row in range(len(grid)):
        for col in range(len(grid[1])):
            print(row, col)
            size = get_island_size(grid, row, col, visited)
            if (size < min_size) and (size > 0):
              min_size = size
    return min_size
        
        
def get_island_size(grid, row, col, visited):
    rowbound = (0 <= row) and (row < len(grid))
    colbound = (0 <= col) and (col < len(grid[1]))
    if not (rowbound and colbound):
        return 0
    if grid[row][col] == 'W': 
        return 0 
    position = str(row)+' '+str(col)
    if position in visited: 
        return 0
    visited.add(position)
    size = 1
    size+= get_island_size(grid, row-1, col, visited)
    size+= get_island_size(grid, row+1, col, visited)
    size+= get_island_size(grid, row, col-1, visited)
    size+= get_island_size(grid, row, col+1, visited)
    return size

grid = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]