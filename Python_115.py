```
def max_fill(grid, capacity):
    total_water = sum(sum(cell == '1' for cell in row) for row in grid)
    return math.ceil(total_water / capacity)

assert max_fill([[str(x) for x in [1, 1, 1, 1]], [str(x) for x in [1, 1, 1, 1]]], 9) == 2