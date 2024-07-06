def minPath(grid, k):
    n = len(grid)
    res = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == k:
                dfs(i, j, [[i * n + j]], [i * j], grid, k, [])
    return res


def dfs(i, j, path, sum_path, grid, k, res):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != k:
        return
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i + x, j + y
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            dfs(
                ni,
                nj,
                path + [[ni * len(grid) + nj]],
                sum_path + [ni * n + nj],
                grid,
                k,
                res,
            )
    if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
        res.append(path)