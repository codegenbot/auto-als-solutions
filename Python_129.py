```
def minPath(grid, k):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    result = None
    def dfs(i, j, path, count):
        nonlocal result
        if count == k:
            if not result or path < result:
                result = path
            return 
        visited[i][j] = True
        for di, dj in directions:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                new_path = dfs(ni, nj, path+[grid[ni][nj]], count+1)
        visited[i][j] = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j, [grid[i][j]], 1)

    return result