int max_fill(vector<vector<int>> grid, int capacity) {
    int n = grid.size();
    vector<int> wells(n, 0);
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < grid[i].size(); j++) {
            if (grid[i][j] == 1) {
                wells[i]++;
            }
        }
    }
    
    int steps = 0;
    while (true) {
        bool changed = false;
        vector<int> new_wells(wells);
        
        for (int i = 0; i < n; i++) {
            if (wells[i] > capacity) {
                wells[i] -= capacity;
                new_wells[i] = 0;
                changed = true;
            } else if (wells[i] > 0) {
                new_wells[i] = 0;
            }
        }
        
        if (!changed) break;
        
        wells = new_wells;
        steps++;
    }
    
    return steps;
}