#include <vector>
#include <utility>
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
    if (grid.empty() || x < 0 || y < 0 || x >= grid.size() || y >= grid[0].size())
        return -1;
    
    if (grid[x][y] == 'O') {
        path.push_back({x, y});
        grid[x][y] = 'X';
        
        int newX = -1;
        int newY = -1;
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                if (grid[i][j] == 'O') {
                    newX = i;
                    newY = j;
                    break;
                }
            }
            if (newX != -1) break;
        }
        
        int ret = pathFinder(grid, newX, newY, path);
        return ret > 0 ? 1 : ret;
    } else {
        return 0;
    }
}