"""
This code was aided using the website below

https://stackoverflow.com/questions/79252013/incrementing-adjacent-mines-
in-minesweeper-using-python/79252977#79252977
"""
# The mine variable is defined
# The minesweeper grid is defined
mine = "#"
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"],
]

# A minesweeper_output function is defined
def minesweeper_output(grid):
   for row in grid:
      for col_i in row:
         print(col_i, end=" ")
      print()
   return

# A border_check function is defined to check each cell
def border_check(grid,row,col):
   if grid[row][col] == mine: return mine
   count = 0
   range_one = range(0, len(grid[0]))
   range_two = range(0, len(grid))
   for check_one in range(col-1,col+2):
      for check_two in range(row-1,row+2):
         if (check_one in range_one) and (check_two in range_two):
           if (check_two,check_one) != (row,col) and grid[check_two][check_one] == mine:
              count += 1
   return count
    
def minesweeper(grid):
   new_grid = grid.copy()
   for i in range(len(new_grid)):
      for j in range(len(new_grid[0])):
        new_grid[i][j] = border_check(new_grid,i,j)
   minesweeper_output(new_grid)
   return new_grid
minesweeper(grid)