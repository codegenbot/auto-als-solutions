#include <vector>
#include <utility>

bool isEqual(std::vector<int> a, std::vector<int> b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); i++)
        if (a[i] != b[i])
            return false;
    return true;
}

int pathFinder(std::vector<std::vector<char>> grid, int x, int y, std::vector<std::pair<int, int>>& path) {
    if (x < 0 || y < 0 || x >= grid.size() || y >= grid[0].size()) {
        return -1; // outside the grid
    }
    if (grid[x][y] == '#') {
        return -1; // obstacle or wall
    }
    path.push_back(std::make_pair(x, y));
    if (x == 0 || y == 0) {
        return 1; // reached the start
    }
    int min = pathFinder(grid, x-1, y, path);
    if (min >= 0)
        return min;
    min = pathFinder(grid, x+1, y, path);
    if (min >= 0)
        return min;
    min = pathFinder(grid, x, y-1, path);
    if (min >= 0)
        return min;
    min = pathFinder(grid, x, y+1, path);
    return min;
}