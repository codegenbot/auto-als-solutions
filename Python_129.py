def minPathSum(grid):
    n = len(grid)
    res = float("inf")
    res_path = []

    def dfs(i, j, path_sum, path):
        nonlocal res, res_path
        if len(path) == (n * n):
            if path_sum < res:
                res = path_sum
                res_path = sorted(path)
            return

        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in path:
                dfs(ni, nj, path_sum + grid[ni][nj], path + [(n * i) + j])

    for i in range(n):
        for j in range(n):
            dfs(i, j, grid[i][j], [(n * i) + j])

    return res_path