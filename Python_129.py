def minPath(grid, k):
    n = len(grid)
    res = []
    
    def dfs(i, j, path):
        if i < 0 or i >= n or j < 0 or j >= n:
            return None
        if grid[i][j] == k and (i == 0 or j == 0 or i == n-1 or j == n-1):
            return path + [k]
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < n:
                new_path = dfs(ni, nj, path + [k])
                if new_path is not None:
                    res.append(new_path)
        return min([p for p in res if p is not None], key=lambda x: len(x))
    
    min_sum = float('inf')
    for i in range(n):
        visited = set()
        visited.add((0, i))
        temp_res = [dfs(0, i, [k])]
        if sum(temp_res[0]) == k:
            return temp_res[0]
        visited.add((n-1, i))
        temp_res = [dfs(n-1, i, [k])]
        if sum(temp_res[0]) == k:
            return temp_res[0]
    for j in range(n):
        visited = set()
        visited.add((i, 0))
        temp_res = [dfs(i, 0, [k])]
        if sum(temp_res[0]) == k:
            return temp_res[0]
        visited.add((i, n-1))
        temp_res = [dfs(i, n-1, [k])]
        if sum(temp_res[0]) == k:
            return temp_res[0]