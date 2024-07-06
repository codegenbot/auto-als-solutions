```
def minPath(grid, k):
    n = len(grid)
    res = []
    def dfs(i, j, path):
        if i == j:
            if sum(path) == k:
                return path
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == k:
                new_path = dfs(nj, j, path + [k])
                res.append(new_path)
        return min([p for p in res if p is not None], key=lambda x: len(x))
    boundary_cells = [(0, j) for j in range(n)] + [(n-1, j) for j in range(n)] + [(i, 0) for i in range(n)] + [(i, n-1) for i in range(n)]
    for i, j in boundary_cells:
        if grid[i][j] == k:
            res = [dfs(i, j, [k])]
    return min([p for p in res if p is not None], key=lambda x: len(x)) or []