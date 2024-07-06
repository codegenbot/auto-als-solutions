def minPath(grid, k):
    N = len(grid)
    values = sum(range(1, N * N + 1), [])
    for i in range(N):
        for j in range(N):
            if grid[i][j] != i * N + j:
                values.insert(i * N + j - 1, None)
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = [(0, [grid[0][0], ])]
    while queue:
        x, path = queue.pop(0)
        if len(path) > k:
            continue
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and len(path) + 1 == k:
                queue.append((nx, path + [grid[nx][ny]]))
    return min(queue)[-1]