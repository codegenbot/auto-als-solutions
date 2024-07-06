def max_fill(grid, capacity):
    rows = [list(row) for row in grid]
    total_water = sum(sum(1 for cell in row if cell == 1) for row in rows)
    return math.ceil(total_water / float(capacity))