vector<int> minPath(vector<vector<int>> grid, int k) {
    int n = grid.size();
    vector<vector<bool>> visited(n, vector<bool>(n));
    vector<int> res;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (!visited[i][j]) {
                vector<int> path;
                dfs(grid, visited, i, j, k, &path);
                if (res.empty() || issame(res, path)) {
                    res = path;
                }
            }
        }
    }
    return res;
}

bool issame(vector<int> a, vector<int> b) {
    return a == b;
}