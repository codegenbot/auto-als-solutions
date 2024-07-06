vector<int> minPath(vector<vector<int>> grid, int k){
    int n = grid.size();
    vector<int> path;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(path.empty() || path.back() < grid[i][j]){
                path.push_back(grid[i][j]);
                while(k > 1 && (i > 0 && path.size() > k) || (j > 0 && path.size() > k)){
                    int last = path.back();
                    for(int x = -1; x <= 1; x++){
                        for(int y = -1; y <= 1; y++){
                            if(x == 0 && y == 0) continue;
                            int newX = i + x, newY = j + y;
                            if(newX >= 0 && newX < n && newY >= 0 && newY < n){
                                path.push_back(grid[newX][newY]);
                                k--;
                            }
                        }
                    }
                }
            } else {
                break;
            }
        }
    }
    return path;
}