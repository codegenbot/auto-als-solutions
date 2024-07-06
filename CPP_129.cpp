```cpp
#ifdef __GXX_EXPERIMENTAL__
#define _SCL_SECURE_NO_WARNINGS
#endif
#include <vector>
#include <utility>

int pathFinder(std::vector<std::vector<char>>& grid, int x, int y, std::vector<std::pair<int, int>>& path) {
    if (grid.empty() || grid[0].empty()) return -1;
    
    // Check the boundaries of the grid
    if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size())
        return -2;

    if (grid[x][y] == 'O') {
        path.push_back({x, y});
        return 1;
    } else {
        return 0;
    }
}

bool isEqual(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); i++)
        if (a[i] != b[i])
            return false;
    return true;
}