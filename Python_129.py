def minPath(grid, k):
    N = len(grid)
    visited = [[False] * N for _ in range(N)]
    min_path = []

    def dfs(x, y, path):
        nonlocal min_path
        if len(path) == k:
            if not min_path or path < min_path:
                min_path = path
            return

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, path + [grid[nx][ny]])
                visited[nx][ny] = False

    for i in range(N):
        for j in range(N):
            visited[i][j] = True
            dfs(i, j, [])
            visited[i][j] = False

    return min_path