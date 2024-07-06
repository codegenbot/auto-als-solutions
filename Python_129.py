def minPath(grid, k):
    n = len(grid)
    memo = {}

    def dfs(i, j, path):
        if (i, j) in memo:
            return memo[(i, j)]

        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n:
                new_path = path + [grid[ni][nj]]
                if len(new_path) == k + 1:
                    memo[(i, j)] = minPathHelper(new_path)
                    return memo[(i, j)]
                elif (ni, nj) not in memo:
                    dfs(ni, nj, new_path)
        memo[(i, j)] = path
        return path

    def minPathHelper(path):
        res = sorted([str(i) for i in path])
        for i in range(len(res)):
            for j in range(i + 1, len(res)):
                if res[i] > res[j]:
                    res[i], res[j] = res[j], res[i]
                    break
            if res == sorted([str(i) for i in path]):
                break
        return [int(i) for i in res]

    min_path = float("inf")
    for i in range(n):
        for j in range(n):
            if (i, j) not in memo:
                path = dfs(i, j, [grid[i][j]])
                if len(path) == k + 1:
                    if path < min_path:
                        min_path = path

    return min_path