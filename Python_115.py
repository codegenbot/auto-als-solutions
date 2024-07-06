def max_fill(grid, capacity):
    row_length = len(grid[0])
    total_water_cells = sum(1 for row in grid if all(cell == 1 for cell in row))
    return min((total_water_cells + capacity - 1) // capacity, len(grid)) if (row_length * len(grid)) >= capacity else len(grid)