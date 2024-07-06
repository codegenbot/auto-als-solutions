vector<int> minPath(vector<vector<int>>& grid, int k) {
    int n = grid.size();
    vector<int> res;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (!res.size() || grid[i][j] > res.back()) {
                res.push_back(grid[i][j]);
            } else if (grid[i][j] == res.back()) {
                res.push_back(grid[i][j]);
                k--;
            }
        }
    }
    
    return res;
}

bool issame(vector<int> a, vector<int> b) {
    return a.size() == b.size() && equal(a.begin(), a.end(), b.begin());
}