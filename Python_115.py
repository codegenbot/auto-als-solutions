```
import math


def max_fill(grid, capacity):
    total_water = sum(row.count(1) * 1 for row in grid)
    return math.ceil(total_water / capacity)

assert max_fill([[1, 1, 1, 1], [1, 1, 1, 1]], 9) == 2