def minPath(grid, k):
    n = len(grid)
    m = [[i for _ in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                return [grid[i][j]] * k
    visited = set()
    res = []
    def dfs(i, j, path):
        if len(path) == k:
            return path
        if (i, j) in visited or i < 0 or i >= n or j < 0 or j >= n:
            return None
        
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                visited.add((i, j))
                res.append(grid[ni][nj])
                path2 = dfs(ni, nj, path + [grid[ni][nj]])
                if path2 is not None:
                    return path2
                visited.remove((i, j))
        return None
    
    for i in range(n):
        for j in range(n):
            res = dfs(i, j, [])
            if res:
                return res