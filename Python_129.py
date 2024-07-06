```
def minPathSum(grid, k):
    n = len(grid)
    res = float('inf')
    path_sum = []

    def dfs(i, j, path, path_sum):
        nonlocal res
        if len(path) == k:
            if path_sum < res[0]:
                res = [path_sum]
            elif path_sum == res[0]:
                res.append(path)
            return

        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in path:
                dfs(ni, nj, path + [(n * i) + j], path_sum + grid[ni][nj])

    for i in range(n):
        for j in range(n):
            dfs(i, j, [], grid[i][j])

    return res[0] if len(res) == 1 else min([len(p) for p in res])