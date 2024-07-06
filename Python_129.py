def minPath(grid, k):
    n = len(grid)
    res = []

    def dfs(i, j, path):
        if len(path) == k:
            return [path]
        if (i, j) in visited or i < 0 or i >= n or j < 0 or j >= n:
            return []
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                new_path = path + [grid[ni][nj]]
                res.extend(dfs(ni, nj, new_path))
        return res

    visited = set()
    result = dfs(0, 0, [])
    for p in result:
        if len(p) == k:
            return p

    return []