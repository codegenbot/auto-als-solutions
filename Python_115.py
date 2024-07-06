import math

def max_fill(grid, capacity):
    total_water = sum(1 for row in grid if 1 in row) * 1
    return math.ceil(total_water / capacity)

assert max_fill([[1, 1, 1, 1], [1, 1, 1, 1]], 9) == 2