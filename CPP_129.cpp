#include <vector>
#include <utility>

int minPath(std::vector<std::vector<char>> grid, int x, int y, std::vector<std::pair<int, int>>& path) {
    if (x<0 || y<0 || x>=grid.size() || y>=grid[0].size()) return -1;
    if (grid[x][y] == 'B') return 0;
    if (grid[x][y] != '.') return -1;

    int minPathLength = INT_MAX;
    for (int dx : {-1, 0, 1}) {
        for (int dy : {-1, 0, 1}) {
            if ((dx==0 && dy==0) || Math.abs(dx)+Math.abs(dy)>2) continue;
            int newX = x + dx;
            int newY = y + dy;
            if (newX>=0 && newX<grid.size() && newY>=0 && newY<grid[0].size()) {
                int newLength = minPath(grid, newX, newY, path);
                if (newLength != -1) {
                    minPathLength = std::min(minPathLength, 1 + newLength);
                }
            }
        }
    }

    if (minPathLength == INT_MAX) return -1;
    else {
        path.push_back(std::make_pair(x,y));
        return 1+minPath(grid,x-dx,y-dy,path);
    }
}