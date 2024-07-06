def minPath(grid, k):
    N = len(grid)
    visited = [[False] * N for _ in range(N)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j, path):
        nonlocal min_path
        if len(path) == k:
            if not min_path or len(path) < len(min_path):
                min_path = path
            return path
        visited[i][j] = True
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                new_path = dfs(ni, nj, path + [grid[i][j]])
                if len(new_path) == k:
                    return new_path
        return min_path

    min_path = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result = dfs(i, j, [])
                if len(result) == k:
                    return result

    return min_path