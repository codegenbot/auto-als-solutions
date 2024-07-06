int max_fill(vector<vector<int>> grid, int capacity) {
    int ans = 0;
    for (const auto& row : grid) {
        int fill = 0;
        for (int i = 0; i < row.size(); ++i) {
            if (row[i] == 1) {
                fill += 1;
            }
        }
        while (fill > 0) {
            fill -= capacity;
            ans++;
        }
    }
    return ans;
}