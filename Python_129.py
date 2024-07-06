```
def minPath(grid, k):
    n = len(grid)
    m = [[i * n + j for j in range(n)] for i in range(n)]
    res = []

    def dfs(i, j, path, sum_path):
        if (i, j) not in visited:
            visited.add((i, j))
            if 0 <= i < n and 0 <= j < n and grid[i][j] == k:
                return [(path + [m[i][j]], sum_path)]
            new_paths = []
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + x, j + y
                if 0 <= ni < n and 0 <= nj < n:
                    new_paths.extend(dfs(ni, nj, path + [m[ni][nj]], sum_path))
            return new_paths

    visited = set()
    for i in range(n):
        visited.add((i, 0))
        visited.add((i, n - 1))
    for j in range(n):
        visited.add((0, j))
        visited.add((n - 1, j))

    min_length = float('inf')
    all_paths = []

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if grid[i][j] == k:
                paths = dfs(i, j, [], 0)
                for path, length in paths:
                    if len(path) < min_length:
                        min_length = len(path)
                        all_paths = [path]
                    elif len(path) == min_length:
                        all_paths.append(path)

    return all_paths