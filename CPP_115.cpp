int max_fill(vector<vector<int>> grid, int capacity) {
    int n = grid.size();
    int ans = 0;
    
    while (true) {
        bool changed = false;
        
        for (int i = 0; i < n; i++) {
            int water = 0;
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j]) {
                    water += 1;
                }
            }
            
            if (water > capacity) {
                int extra_water = water - capacity;
                
                for (int j = 0; j < grid[i].size(); j++) {
                    if (grid[i][j] && --extra_water >= 0) {
                        grid[i][j] = 0;
                    }
                }
                
                changed = true;
            } else {
                break;
            }
        }
        
        if (!changed) {
            break;
        }
        
        ans++;
    }
    
    return ans;
}