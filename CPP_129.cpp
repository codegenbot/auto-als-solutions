```cpp
#include <vector>
#include <utility>

int pathFinder(std::vector<std::vector<char>>& grid, int x, int y, std::vector<std::pair<int, int>>& path) {
    if (grid.empty() || grid[0].empty()) return -1;
    
    // Check the boundaries of the grid
    if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size())
        return -2;

    std::vector<std::pair<int, int>> pathFound = {{x, y}};

    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            if (i == 0 && j == 0) continue;

            int newX = x + i;
            int newY = y + j;

            if (newX >= 0 && newX < grid.size() && newY >= 0 && newY < grid[0].size()) {
                if (grid[newX][newY] == 'O') {
                    pathFound.push_back({newX, newY});
                    return 1;
                }
            }
        }
    }

    return 0;
}

bool isEqual(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); i++)
        if (a[i] != b[i])
            return false;
    return true;
}