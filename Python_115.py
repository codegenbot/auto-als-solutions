```
def max_fill(grid, capacity):
    rows = [list(row) for row in grid]
    total_water = sum(1 for row in rows for cell in row if cell == 1)
    return math.ceil(total_water / capacity)