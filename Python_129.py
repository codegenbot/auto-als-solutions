def minPath(grid, k):
    n = len(grid)
    res = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(grid, i, j, k, [grid[i][j]], res)
    return res


def dfs(grid, x, y, k, path, res):
    n = len(grid)
    if k == 0:
        res.append(path[:])
        return
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in path:
                grid[nx][ny], grid[x][y] = grid[x][y], grid[nx][ny]
                dfs(grid, nx, ny, k - 1, path + [(nx, ny)], res)
                grid[nx][ny], grid[x][y] = grid[x][y], grid[nx][ny]