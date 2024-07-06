def max_fill(grid, capacity):
    total_water = sum(len([cell for cell in row if cell == 1]) for row in grid)
    return math.ceil(total_water / capacity)