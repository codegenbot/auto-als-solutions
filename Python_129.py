def minPath(grid, k):
    n = len(grid)
    m = [[i * n + j for j in range(n)] for i in range(n)]
    visited = set()
    min_paths = []

    def dfs(i, j, path, sum_path):
        if (i, j) in visited:
            return None
        if 0 <= i < n and 0 <= j < n and grid[i][j] == k:
            return ((path + [m[i][j]]), sum_path + k)
        if 0 <= i < n and 0 <= j < n and grid[i][j] != k:
            return None
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n:
                new_path, new_sum = dfs(ni, nj, path + [m[ni][nj]], sum_path + k)
                min_paths.append(new_path)
        return (min_paths, min(min_paths, key=lambda x: sum(x)))

    min_paths, _ = dfs(0, 0, [], 0)