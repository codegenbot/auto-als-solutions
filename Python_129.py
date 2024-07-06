def minPath(grid, k):
    N = len(grid)
    visited = [[False] * N for _ in range(N)]
    queue = [(0, 0, [grid[0][0]])]
    result = []

    while queue:
        x, y, path = queue.pop(0)
        if len(path) > k:
            continue
        if len(path) == k:
            result = sorted(list(set(path)))
            return result

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, path + [grid[nx][ny]]))
        for cell in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= cell[0] < N and 0 <= cell[1] < N:
                queue.insert(0, cell + [grid[cell[0]][cell[1]]])