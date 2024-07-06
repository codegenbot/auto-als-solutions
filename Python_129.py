```
def minPath(grid, k):
    n = len(grid)
    visited = [[False]*n for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j, path, count):
        if count == k:
            return path
        visited[i][j] = True
        min_path = path[:]
        for di, dj in directions:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                new_path = dfs(ni, nj, path+[grid[ni][nj]], count+1)
                if not min_path or new_path < min_path:
                    min_path = new_path
        visited[i][j] = False
        return min_path

    result = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                path = dfs(i, j, [grid[i][j]], 1)
                if not result or path < result:
                    result = path

    return result