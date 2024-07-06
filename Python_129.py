def minPath(grid, k):
    n = len(grid)
    res = []
    
    def dfs(i, j, path, sum_path):
        nonlocal res
        if (i, j) in [(x, y) for x in range(n) for y in range(n)]:
            return None
        visited[(i, j)] = True
        if 0 <= i < n and 0 <= j < n and grid[i][j] == k:
            if not res or len(path) + 1 < min(len(x) for x in res):
                res.append(path + [k])
            return None
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n:
                new_path, new_sum = dfs(ni, nj, path + [k], sum_path + k)
                if new_path:
                    res.append(new_path)
        return None
    
    visited = {(x, y) for x in range(n) for y in range(n)}
    dfs(0, 0, [], 0)
    return min(res, key=len)