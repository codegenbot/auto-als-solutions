def minPath():
    grid = [[int(x) for x in input().split(',')] for _ in range(int(input()))]
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
                if new_path:
                    min_paths.append(new_path)
        return (
            min([p for p in set(tuple(x) for x in min_paths) if p], key=lambda x: len(x))
            or []
        )

    boundary_cells = [(0, j) for j in range(n)] + [(n - 1, j) for j in range(n)] + [(i, 0) for i in range(n)] + [(i, n - 1) for i in range(n)]
    min_path = []
    k = int(input("Enter a number: "))
    visited.add((0, 0))
    paths = [p for p in [dfs(0, 0, [m[0][0]], k)] if p] 
    for path in set(tuple(x) for x in paths):
        if path:
            min_path = min([path], key=lambda x: len(x))
            break

    return min_path if min_path else []