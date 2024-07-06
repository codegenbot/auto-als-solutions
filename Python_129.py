def minPath(grid, k):
    n = len(grid)
    visited = set()
    min_paths = []

    def dfs(i, j, path, sum_path):
        if (i, j) in visited:
            return None
        visited.add((i, j))
        if 0 <= i < n and 0 <= j < n:
            if grid[i][j] == k:
                return ((path + [(i, j)]), sum_path + k)
            if 0 <= i < n - 1:
                new_path = dfs(i + 1, j, path + [(i, j)], sum_path + k)
                if new_path:
                    min_paths.append(new_path[0])
            if i > 0:
                new_path = dfs(i - 1, j, path + [(i, j)], sum_path + k)
                if new_path:
                    min_paths.append(new_path[0])
            if 0 <= j < n - 1:
                new_path = dfs(i, j + 1, path + [(i, j)], sum_path + k)
                if new_path:
                    min_paths.append(new_path[0])
            if j > 0:
                new_path = dfs(i, j - 1, path + [(i, j)], sum_path + k)
                if new_path:
                    min_paths.append(new_path[0])
        return (
            min(
                [p for p in set(tuple(x) for x in min_paths) if p], key=lambda x: len(x)
            )
            or []
        )

    min_path = []
    for i in range(n):
        visited.add((i, 0))
        paths = [p for p in [dfs(i, 0, [(i, 0)], k)] if p]
        for path in set(tuple(x) for x in paths):
            if path:
                min_path = min([path], key=lambda x: len(x))
                break
    for j in range(n):
        visited.add((0, j))
        paths = [p for p in [dfs(0, j, [(0, j)], k)] if p]
        for path in set(tuple(x) for x in paths):
            if path:
                min_path = min([path], key=lambda x: len(x))
                break

    return min_path if min_path else []