vector<int> minPath(vector<vector<int>> grid, int k) {
    vector<pair<vector<int>, int>> memo(grid.size() * grid[0].size(), make_pair(vector<int>(), 0));
    
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            int val = grid[i][j];
            if (k == 1) {
                memo[i * grid[0].size() + j] = make_pair(vector<int>(1, val), 0);
            } else {
                vector<pair<vector<int>, int>> newMemo;
                for (int x = -1; x <= 1; x++) {
                    for (int y = -1; y <= 1; y++) {
                        if (i + x >= 0 && i + x < grid.size() && j + y >= 0 && j + y < grid[0].size()) {
                            int val2 = grid[i + x][j + y];
                            if (k > 1) {
                                for (auto &p : memo[(i * grid[0].size() + j) % (grid.size() * grid[0].size())]) {
                                    p.first.push_back(val2);
                                    p.second++;
                                    newMemo.emplace_back(move(p));
                                }
                            } else {
                                newMemo.emplace_back(make_pair(vector<int>(1, val2), 1));
                            }
                        }
                    }
                }
                memo[(i * grid[0].size() + j) % (grid.size() * grid[0].size())] = min_element(newMemo.begin(), newMemo.end());
            }
        }
    }
    
    return memo[0].first;
}