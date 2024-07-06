def minPath(grid, k):
    N = len(grid)
    visited = [[False] * N for _ in range(N)]
    path = []

    def dfs(i, j, curr_path):
        nonlocal path
        if len(curr_path) == k:
            path = sorted(curr_path)
            return True

        if visited[i][j] or (i, j) in [
            (x, y) for x, row in enumerate(visited) for y, val in enumerate(row) if val
        ]:
            return False

        visited[i][j] = True
        curr_path.append(grid[i][j])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N:
                if dfs(ni, nj, curr_path[:]):
                    return True

        visited[i][j] = False
        return False

    for i in range(N):
        for j in range(N):
            if dfs(i, j, []):
                return path