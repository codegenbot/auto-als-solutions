```
def minPath(grid, k):
    n = len(grid)
    m = [[i * n + j for j in range(n)] for i in range(n)]
    dp = [[[float('inf'), []] for _ in range(n * n)] for _ in range(n * n)]
    dp[0][0][0] = 0
    for i in range(1, n):
        dp[i][0][0] = dp[i - 1][0][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j][0] = dp[0][j - 1][0] + grid[0][j]
    for i in range(1, n):
        for j in range(1, n):
            if dp[(i-1)*n+j][j-1][0]+grid[i][j] <= dp[i*n+j][(i-1)*n+j-1][0]+grid[i][j]:
                dp[i*n+j][m[i-1][j]][0] = dp[i*n+j][j-1][0]+grid[i][j]
            else:
                dp[i*n+j][m[i-1][j]][0] = dp[(i-1)*n+j-1][0]+grid[i][j]
    for i in range(n):
        for j in range(n):
            if dp[n-1][n-1][0] == dp[m[i][j]][m[i][j]][0]+k:
                return [[grid[x][y] for x, y in [(i, j)] + path] for path in [dp[k][j][1] for k in range(n*n) if dp[k][j][0] == dp[n-1][n-1][0]+k][0]]
    return []