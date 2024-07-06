import math


def max_fill(grid, capacity):
    total_water = sum(sum(row) for row in grid)
    fill_count = math.ceil(total_water / capacity)
    return fill_count