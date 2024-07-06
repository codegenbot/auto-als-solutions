def minPath(grid, k):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            grid[i][j] *= i + j
    return grid