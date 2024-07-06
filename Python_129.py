def minPath(grid, k):
    n = len(grid)
    res = []

    def dfs(i, j, path, total):
        nonlocal res
        if len(path) == k:
            if not res or total < sum(res[0]):
                res = [path]
            elif total == sum(res[0]):
                res.append(path)
            return

        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in set(path):
                dfs(ni, nj, path + [(n * i) + j], total + grid[ni][nj])

    for i in range(n):
        for j in range(n):
            dfs(i, j, [], grid[i][j])

    return res[0]