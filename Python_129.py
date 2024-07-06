def minPath(grid, k):
    N = len(grid)
    visited = [[False] * N for _ in range(N)]
    queue = [(0, 0, [grid[0][0]])]
    result = []

    while queue:
        k_count = 0
        x, y, path = queue.pop(0)
        for p in path[1:]:
            k_count += grid[x][y] == int(p)
        if k_count > k:
            return []
        if len(path) == k:
            result = sorted(list(set(path)))
            return result

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, path + [grid[nx][ny]]))

    return []