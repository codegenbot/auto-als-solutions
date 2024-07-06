```
def minPath(grid):
    n = len(grid)
    dp = [[0] * (n + k) for _ in range(n + k)]
    for i in range(k):
        for j in range(n + i, n + k):
            dp[j - i][j] = 1
    for i in range(1, n + k):
        for j in range(1, n + k):
            if grid[i - 1][j - 1]:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
            elif i >= k and j >= k:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    path = []
    i, j = n + k - 1, n + k - 1
    while (i > 0 or j > 0) and (i < k or j < k):
        if i > 0 and (j == 0 or grid[i-1][j] == grid[i][j]):
            i -= 1
        elif j > 0 and (i == 0 or grid[i][j-1] == grid[i][j]):
            j -= 1
        else:
            if i > 0 and dp[i-1][j] < dp[i][j-1]:
                path.append(grid[i-1][j])
                i -= 1
            else:
                path.append(grid[i][j-1])
                j -= 1
    return list(reversed(path))