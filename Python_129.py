def minPath(grid, k):
    n = len(grid)
    m = [[i * n + j for j in range(n)] for i in range(n)]

    def dfs(i, j, path):
        if len(path) == k:
            return path
        res = float("inf")
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n and m[ni][nj] not in path:
                p = dfs(ni, nj, path + [m[ni][nj]])
                res = min(res, p) if len(p) == k else res
        return res

    res = []
    for i in range(n):
        for j in range(n):
            p = dfs(i, j, [])
            if len(p) == k:
                res = p
                break
        if res:
            break
    return res