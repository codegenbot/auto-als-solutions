#include <initializer_list>

bool isEqual(std::vector<int> a, std::vector<int> b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); i++)
        if (a[i] != b[i])
            return false;
    return true;
}

int pathFinder(std::vector<std::vector<char>> grid, int x, int y, std::vector<std::pair<int, int>>& path) {
    if (!grid[x][y]) {
        path.push_back({x, y});
        for (int i = -1; i <= 1; ++i) {
            for (int j = -1; j <= 1; ++j) {
                if (std::abs(i) + std::abs(j) > 1) continue;
                int newX = x + i;
                int newY = y + j;
                if (newX >= 0 && newX < grid.size() && newY >= 0 && newY < grid[0].size()) {
                    if (!grid[newX][newY]) {
                        pathFinder(grid, newX, newY, path);
                    }
                }
            }
        }
    }
}