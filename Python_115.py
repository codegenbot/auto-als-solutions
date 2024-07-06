def max_fill(grid, capacity):
    total_water = sum(sum(row) for row in grid)
    fill_count = -(-total_water // capacity)
    return fill_count