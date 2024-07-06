```
def minPath(grid, k):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    res = []
    def dfs(i, j, path):
        nonlocal res
        if len(path) == k:
            res = sorted(path)
            return True
        if (i < 0 or i >= n or j < 0 or j >= n or visited[i][j]):
            return False
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + x, j + y
            if dfs(ni, nj, path + [grid[i][j]]):
                return True
        visited[i][j] = True
    for i in range(n):
        for j in range(n):
            dfs(i, j, [])
    return res