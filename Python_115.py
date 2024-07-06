```Python
def max_fill(grid, capacity):
    total_water = 0
    for i in range(1, len(grid) - 1):
        for j in range(len(grid[i])):
            if grid[i][j] == 1 and (grid[i-1][j] == 1 or grid[i+1][j] == 1 or 
                                    grid[i][j-1] == 1 or grid[i][j+1] == 1):
                total_water += 1
    return math.ceil(total_water / capacity)