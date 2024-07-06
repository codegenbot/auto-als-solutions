import math
def max_fill(grid, capacity):
    total_water = sum(sum(row) for row in grid)
    fill_count = math.ceil(total_water / capacity)
    return int(fill_count) if fill_count > 0 else 0