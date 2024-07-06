#include <vector>
#include <utility>

int pathFinder(std::vector<std::vector<char>>& grid, int x, int y, std::vector<std::pair<int, int>>& path) {
    if (grid.empty() || grid[0].empty()) return -1;
    
    // Your implementation here
    
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

int main() {
    std::vector<std::vector<char>> grid = {{1, 3}, {3, 2}};
    int x = -1, y = -1;
    std::vector<std::pair<int, int>> path;
    if (pathFinder(grid, x, y, path) == -1) {
        assert(false);
    } else {
        assert(isEqual(path, {0, 0, 1, 2, 1, 3, 1, 3, 1, 3}));
    }
    return 0;
}