#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> minPath(vector<vector<int>>& grid, int k) {
    vector<pair<int, pair<int, int>>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    vector<vector<bool>> visited(grid.size(), vector<bool>(grid[0].size()));
    priority_queue<pair<int, vector<int>>, vector<pair<int, vector<int>>>, greater<pair<int, vector<int>>>> pq;
    for (int i = 0; i < grid.size(); ++i) {
        for (int j = 0; j < grid[i].size(); ++j) {
            if (!visited[i][j]) {
                visited[i][j] = true;
                pq.push({grid[i][j], {grid[i][j]}});
            }
        }
    }

    vector<int> res;
    while (!pq.empty()) {
        int val = pq.top().first;
        res = pq.top().second;
        pq.pop();
        if (res.size() == k) {
            break;
        }
        for (auto& dir : directions) {
            int ni = res.back() + dir.first;
            int nj = res.back() + dir.second;
            if (ni >= 0 && ni < grid.size() && nj >= 0 && nj < grid[0].size() && !visited[ni][nj]) {
                visited[ni][nj] = true;
                pq.push({grid[ni][nj], res});
            }
        }
    }

    return res;
}