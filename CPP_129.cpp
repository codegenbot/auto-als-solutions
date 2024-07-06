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
    std::vector<std::vector<char>> grid = {{'A', 'B'}, {'C', 'D'}};
    int x = 10, y = 10;
    std::vector<std::pair<int, int>> path;
    
    int result = pathFinder(grid, x, y, path);
    
    assert(isEqual({1, 3, 1, 3}, {1, 3, 1, 3, 1, 3, 1, 3, 1, 3}));
    
    return 0;
}