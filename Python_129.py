def minPath(grid, k):
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j, path):
        if len(path) == k:
            return path
        visited[i][j] = True
        min_path = None
        for direction in directions:
            ni, nj = i + direction[0], j + direction[1]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                new_path = path + [grid[ni][nj]]
                min_path = dfs(ni, nj, new_path) or min_path
        visited[i][j] = False
        return min_path

    start_points = [(i, j) for i in range(n) for j in range(m)]
    min_paths = []
    for i, j in start_points:
        path = dfs(i, j, [grid[i][j]])
        if path and (not min_paths or min_paths[0] > path):
            min_paths = [path]

    return min_paths[0]