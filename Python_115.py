def max_fill(grid, capacity):
    total_water = sum(1 for row in grid for cell in row if cell == 1)
    return min((total_water + capacity - 1) // capacity, len(grid))