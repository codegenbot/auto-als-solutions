```Python
import math

def max_fill(grid, capacity):
    rows = [row.count(1) for row in grid]
    return math.ceil(sum(rows) / capacity)