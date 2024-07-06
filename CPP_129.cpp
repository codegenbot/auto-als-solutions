#include <vector>
#include <utility>

int minPath(vector<vector<char>> grid, int x, int y, vector<pair<int, int>>& path) {
    if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size() || grid[x][y] == 'X') {
        return -1;
    }
    
    if (grid[x][y] == 'O' && x == y) {
        vector<pair<int, int>> tempPath = {{x, y}};
        path = tempPath;
        return 1;
    }
    
    grid[x][y] = 'X';
    int left = minPath(grid, x-1, y, path);
    if (left < 0) {
        int right = minPath(grid, x+1, y, path);
        if (right < 0) {
            int up = minPath(grid, x, y-1, path);
            if (up < 0) {
                int down = minPath(grid, x, y+1, path);
                return down;
            }
            else {
                grid[x][y-1] = 'O';
                return up;
            }
        }
        else {
            grid[x+1][y] = 'O';
            return right;
        }
    }
    else {
        grid[x-1][y] = 'O';
        return left;
    }
}