vector<int> minPath(vector<vector<int>>& grid, int k) {
    vector<int> result;
    for (int i = 0; i < k; i++) {
        bool updated = false;
        for (int j = 0; j < grid.size(); j++) {
            for (int col = 0; col < grid[0].size(); col++) {
                if (result.empty() || grid[j][col] == result.back()) {
                    vector<int> path(j, col);
                    int value = 1;
                    bool validPath = true;
                    for (int index = 1; index <= k; index++) {
                        value++;
                        if (index + j < 0 || index + j >= grid.size() || 
                            index + col < 0 || index + col >= grid[0].size()) {
                            validPath = false;
                            break;
                        }
                        bool found = false;
                        for (int pathIndex = 0; !found && pathIndex < i; pathIndex++) {
                            if (path[pathIndex] == j && path[colIndex] == col) {
                                found = true;
                            } else if (path[pathIndex] + j >= grid.size() || 
                                       path[pathIndex] + col >= grid[0].size()) {
                                validPath = false;
                                break;
                            }
                        }
                        if (!found) {
                            for (int row = 0; row < grid.size(); row++) {
                                for (int colIndex = 0; colIndex < grid[0].size(); colIndex++) {
                                    if (grid[row][colIndex] == value && 
                                       !found && !isVisited(path, row, colIndex)) {
                                        j = row;
                                        col = colIndex;
                                        found = true;
                                        break;
                                    }
                                }
                                if (found) {
                                    break;
                                }
                            }
                        }
                    }
                    if (!validPath || !result.empty() && result.back() < grid[j][col]) {
                        continue;
                    }
                    result.push_back(grid[j][col]);
                    updated = true;
                    break;
                }
            }
        }
    }
    return result;
}