def minPath(grid, k):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]

    def dfs(i, j, path, count):
        if count == k:
            return [path]

        visited[i][j] = True
        paths = []
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                new_path = path + [grid[ni][nj]]
                new_paths = dfs(ni, nj, new_path, count + 1)
                for p in new_paths:
                    paths.append(p)
        visited[i][j] = False
        return sorted(paths)

    min_paths = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                paths = dfs(i, j, [], 0)
                if not min_paths or min_paths[0] > paths[0]:
                    min_paths = [p for p in paths]

    return min_paths[0]