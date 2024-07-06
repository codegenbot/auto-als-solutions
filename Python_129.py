```
def minPath(grid, k):
    n = len(grid)
    res = []

    def dfs(i, j, path, sum_path):
        nonlocal res
        if len(path) == k:
            if not res or sum_path < sum(res):
                res = path
            return

        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in path:
                dfs(ni, nj, path + [(n * i) + j], sum_path + grid[ni][nj])

    for i in range(n):
        for j in range(n):
            dfs(i, j, [], 0)

    return res