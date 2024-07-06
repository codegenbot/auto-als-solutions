```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> minPath(vector<vector<int>>& grid, int k) {
    int n = grid.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            dp[i][j] = grid[i][j];

    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
    pq.push({grid[0][0], {0, 0}});
    vector<vector<bool>> visited(n, vector<bool>(n));
    visited[0][0] = true;

    while (!pq.empty()) {
        auto [val, pos] = pq.top();
        pq.pop();

        if (k == 0) break;
        k--;

        int x = pos.second, y = pos.first;
        for (int dx = -1; dx <= 1; ++dx)
            for (int dy = -1; dy <= 1; ++dy) {
                int nx = x + dx, ny = y + dy;
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    pq.push({val - dp[nx][ny], {nx, ny}});
                }
            }

        if (k == 0) break;
    }

    vector<int> res;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (!visited[i][j]) {
                res.push_back(grid[i][j]);
                k--;
                while (k > 0) {
                    int dx = -1;
                    do {
                        x += dx, y += (dx == 1 ? -1 : 1);
                    } while (x < 0 || x >= n || y < 0 || y >= n || !visited[x][y]);
                    visited[x][y] = false;
                    res.push_back(grid[x][y]);
                    k--;
                }
            }

    return res;
}

int main() {
    vector<vector<int>> grid = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int k = 3;
    vector<int> result = minPath(grid, k);
    for (auto x : result)
        cout << x << " ";
    return 0;
}