def minPath(grid, k):
    N = len(grid)
    visited = [[False] * N for _ in range(N)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j, path):
        if len(path) == k:
            return path
        visited[i][j] = True
        min_path = path[:]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                new_path = dfs(ni, nj, path + [grid[i][j]])
                if len(new_path) == k:
                    return new_path
        return min_path

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result = dfs(i, j, [])
                if len(result) < k:
                    min_length = float('inf')
                    shortest_path = []
                    for path in [result]:
                        if len(path) == k and len(path) < min_length:
                            min_length = len(path)
                            shortest_path = path
                    return shortest_path
    return []