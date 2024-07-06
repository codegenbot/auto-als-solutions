#include <iostream>
#include <vector>
#include <array>

using namespace std;

bool isSame(const pair<int, int>& p1, const pair<int, int>& p2) {
    return p1.first == p2.first && p1.second == p2.second;
}

int minPath(vector<vector<char>>& grid, int x, int y, vector<pair<int, int>>& path) {
    if (x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size() || grid[x][y] == 'X') {
        return -1;
    }

    if (!isSame({x, y}, {0, 0})) {
        path.push_back({x, y});
    }

    grid[x][y] = 'X';

    if (x == 0 && y == 0) {
        return 1;
    }

    int minDist = -1;
    for (const auto& dir : {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}) {
        int newX = x + dir.first;
        int newY = y + dir.second;
        if (minPath(grid, newX, newY, path) != -1) {
            if (minDist == -1 || minPath(grid, newX, newY, path) < minDist) {
                minDist = minPath(grid, newX, newY, path);
            }
        }
    }

    return minDist;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<char>> grid(n, vector<char>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            char c;
            cin >> c;
            grid[i][j] = c;
        }
    }

    int res = minPath(grid, n - 1, m - 1, vector<pair<int, int>>());
    if (res != -1) {
        cout << "The shortest path length is: " << res << endl;
    } else {
        cout << "No path exists" << endl;
    }

    return 0;
}