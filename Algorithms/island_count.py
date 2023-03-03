def island_count(grid):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[1])):
            if explore_land(grid, row, col, visited) == True:
               count += 1
    return count
        
        
def explore_land(grid, row, col, visited):
    rowbound = (0 <= row) and (row < len(grid))
    colbound = (0 <= col) and (col < len(grid[1]))
    if not (rowbound and colbound):
        return False
    if grid[row][col] == 'W': 
        return False 
    pos = str(row)+' '+str(col)
    if pos in visited: 
        return False
    visited.add(pos)
    explore_land(grid, row-1, col, visited)
    explore_land(grid, row+1, col, visited)
    explore_land(grid, row, col-1, visited)
    explore_land(grid, row, col+1, visited)
    return True
        
        

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]