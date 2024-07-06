int minPath(std::vector<std::pair<int, int>>& path) {
    if (path.empty()) return 0;
    
    std::pair<int, int> prev = path[0];
    for (int i = 1; i < path.size(); i++) {
        if ((abs(path[i].first - prev.first) + abs(path[i].second - prev.second)) > 1)
            return -1;
        prev = path[i];
    }
    
    return 0;
}

int pathFinder(std::vector<std::vector<char>>& grid, int x, int y, std::vector<std::pair<int, int>>& path) {
    if (grid.empty() || grid[0].empty()) return -1;
    
    // Check the boundaries of the grid
    if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size())
        return -2;

    // Your implementation here
    
    int result = pathFinderHelper(grid, x, y, path);
    
    return minPath(path) ? result : -1;
}

int pathFinderHelper(std::vector<std::vector<char>>& grid, int x, int y, std::vector<std::pair<int, int>>& path) {
    if (grid.empty() || grid[0].empty()) return 0;
    
    if (!isValid(grid, x, y))
        return 0;
    
    if (isEnd(grid, x, y)) {
        return path.size();
    }
    
    for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
            if ((dx == 0) && (dy == 0))
                continue;
            
            int newX = x + dx;
            int newY = y + dy;
            
            if (!isValid(grid, newX, newY))
                continue;
            
            char c = grid[newX][newY];
            if (c != '#') {
                grid[newX][newY] = '#';
                path.push_back(std::make_pair(newX, newY));
                int result = pathFinderHelper(grid, newX, newY, path);
                if (result > 0) {
                    return 1 + result;
                }
            }
        }
    }
    
    return 0;
}

bool isValid(const std::vector<std::vector<char>>& grid, int x, int y) {
    return (x >= 0 && x < grid.size() && y >= 0 && y < grid[0].size());
}

bool isEnd(const std::vector<std::vector<char>>& grid, int x, int y) {
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == 'E')
                return true;
        }
    }
    
    return false;
}