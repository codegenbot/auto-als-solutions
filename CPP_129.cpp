#include <vector>
#include <array>

using namespace std;

bool issame(int a1, int b1, int a2, int b2) {
    if ((a1 == a2 && b1 == b2)) return true;
    return false;
}

int minPath(vector<vector<int>>& grid, vector<pair<int,int>>& minPath) {
    int n = grid.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (!minPath.empty() && issame(i, j, minPath.back().first, minPath.back().second)) {
                continue;
            }
            int val = grid[i][j];
            if (val == 1) {
                minPath.push_back({i,j});
            } else {
                for (auto& dir : {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}) {
                    int x = i + dir[0];
                    int y = j + dir[1];
                    if (x >= 0 && x < n && y >= 0 && y < n && grid[x][y] == val - 1) {
                        vector<pair<int,int>> path = minPath;
                        path.push_back({x,y});
                        return minPathPath(grid, path);
                    }
                }
            }
        }
    }
    return 0;
}