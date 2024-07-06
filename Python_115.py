def max_fill(grid, capacity):
    rows = [
        [
            min(max(grid[i][j], grid[i + 1][j]), grid[i][j + 1]) - grid[i][j]
            for j in range(len(grid[0]))
        ]
        for i in range(len(grid) - 1)
    ]
    return sum(sum(row) // capacity for row in rows)