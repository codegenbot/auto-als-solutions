#include <vector>
#include <utility>

int pathFinder(std::vector<std::vector<char>>& grid, int x, int y, std::vector<std::pair<int, int>>& path) {
    if (grid.empty() || grid[0].empty()) return -1;
    
    // Check the boundaries of the grid
    if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size())
        return -2;

    int minPath = INT_MAX;
    for (int dx : {-1, 0, 1}) {
        for (int dy : {-1, 0, 1}) {
            if (dx == 0 && dy == 0) continue;
            
            int newX = x + dx;
            int newY = y + dy;
            
            // Check the boundaries of the grid
            if (newX < 0 || newX >= grid.size() || newY < 0 || newY >= grid[0].size())
                continue;
            
            if (grid[newX][newY] == 'O') {
                std::vector<std::pair<int, int>> pathFound = {{x, y}, {newX, newY}};
                
                // Check for same paths
                bool foundSamePath = false;
                for (int i = 0; i < path.size(); i++) {
                    if (isEqual(path[i], pathFound[1])) {
                        foundSamePath = true;
                        break;
                    }
                }
                
                if (!foundSamePath) {
                    int tempMinPath = 1 + pathFinder(grid, newX, newY, path);
                    if (tempMinPath > 0 && tempMinPath < minPath)
                        minPath = tempMinPath;
                }
            }
        }
    }
    
    return minPath;
}

bool isEqual(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); i++)
        if (a[i] != b[i])
            return false;
    return true;
}