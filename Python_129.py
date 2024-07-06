def minPathSum(grid):
    n = len(grid)
    res = float("inf")
    prev_sum = 0
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                prev_sum += grid[i][j]
            elif j == 0:
                prev_sum += grid[i][j]
            else:
                prev_sum += grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
            if prev_sum < res:
                res = prev_sum
    return res