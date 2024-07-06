def minPath(grid, k):
    n = len(grid)
    m = [(i, j) for i in range(n) for j in range(n)]

    def dfs(i, j, path, visited):
        if len(path) == k:
            return path
        visited.add((i, j))
        paths = []
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                new_path = path + [grid[ni][nj]]
                paths.append(dfs(ni, nj, new_path, visited.copy()))
        return min(paths, key=lambda x: list(x))

    return dfs(0, 0, [], set())[1:]