def minPath(grid, k):
    n = len(grid)
    m = [[i for _ in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            m[i][j] = (m[i][j], grid[i][j])

    def dfs(i, j, path, visited):
        if len(path) == k:
            return path
        if (i, j) in visited or (i < 0 or i >= n or j < 0 or j >= n):
            return None

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                path.append(grid[ni][nj])
                res = dfs(ni, nj, path[:], visited | {(i, j), (ni, nj)})
                if res is not None:
                    return res
                path.pop()
        return None

    min_path = None
    for i in range(n):
        for j in range(n):
            path = [grid[i][j]]
            res = dfs(i, j, path, {(i, j)})
            if res is not None and (min_path is None or res < min_path):
                min_path = res

    return min_path