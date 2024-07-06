def minPath(grid, k):
    n = len(grid)
    res = float("inf"), None
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(i, j, path_sum, path):
        nonlocal res
        if len(path) == k:
            if path_sum < res[0]:
                res = (path_sum, path)
            return

        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in set(path):
                dfs(ni, nj, path_sum + grid[ni][nj], path + [(n * i) + j])

    for i in range(n):
        for j in range(n):
            dfs(i, j, grid[i][j], [(n * i) + j])

    return res[1]