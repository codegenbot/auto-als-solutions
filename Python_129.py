def minPath(grid, k):
    n = len(grid)
    m = [[i * n + j for j in range(n)] for i in range(n)]
    visited = set()
    res = []
    
    def dfs(i, j, path, sum_path):
        if (i, j) in visited:
            return None
        if 0 <= i < n and 0 <= j < n and grid[i][j] == k:
            return ((path), sum_path)
        if 0 <= i < n and 0 <= j < n and grid[i][j] != k:
            return None
        total_sum_path = sum_path + k
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n:
                new_path, new_sum = dfs(ni, nj, path + [m[ni][nj]], total_sum_path)
                if new_path:
                    res.append([x for x in new_path])
        return (min([p for p in set(tuple(x) for x in res) if p], key=lambda x: len(x)) or [])