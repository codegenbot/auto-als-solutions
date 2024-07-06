def minPath(grid, k):
    N = len(grid)
    visited = [[False] * N for _ in range(N)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j, path):
        nonlocal min_path
        if len(path) == k:
            if not min_path or len(path) < len(min_path):
                min_path = path[:]
            return
        visited[i][j] = True
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                dfs(ni, nj, path + [grid[i][j]])
        visited[i][j] = False

    min_path = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, [])
    return min_path