def minPath(grid, k):
    n = len(grid)
    m = [[i * n + j for j in range(n)] for i in range(n)]
    visited = set()
    min_paths = []

    def dfs(i, j, path, sum_path):
        nonlocal min_paths
        if (i, j) in visited:
            return None
        visited.add((i, j))
        if 0 <= i < n and 0 <= j < n and grid[i][j] == k:
            min_paths.append(path)
            return [(path, sum_path)]
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n:
                new_path, new_sum = dfs(ni, nj, path + [m[ni][nj]], sum_path + k)
                if new_path:
                    return [(p, s) for p, s in new_path] + [(path, sum_path)]
        return []

    def find_min_path(grid, k):
        n = len(grid)
        m = [[i * n + j for j in range(n)] for i in range(n)]
        visited = set()
        min_paths = []

        for i in range(n):
            for j in range(n):
                if (i, j) not in visited:
                    paths = [p for p in [dfs(i, j, [m[i][j]], k)] if p]
                    for path in set(tuple(x) for x in paths):
                        min_path = min([p for p in path], key=lambda x: len(x))
                        break

        return min(min_paths, key=lambda x: len(x)) or []

    return find_min_path(grid, k)