#include <vector>
#include <algorithm>

using namespace std;

vector<int> minPath(vector<vector<int>> grid, int k) {
    int n = grid.size();
    vector<vector<bool>> visited(n, vector<bool>(n));
    vector<int> res;
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (!visited[i][j]) {
                vector<int> path;
                dfs(grid, visited, i, j, k, path);
                res = minPath(res, path);
            }
        }
    }
    
    return res;
}

vector<int> minPath(vector<int> v1, vector<int> v2) {
    for (int i = 0; i < min(v1.size(), v2.size()); ++i) {
        if (v1[i] < v2[i]) {
            return v1;
        } else if (v1[i] > v2[i]) {
            return v2;
        }
    }
    
    return v1.size() <= v2.size() ? v1 : v2;
}

void dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int i, int j, int k, vector<int>& path) {
    if (k == 0) {
        return;
    }
    
    path.push_back(grid[i][j]);
    
    for (int x = max(0, i - 1); x <= min(i + 1, grid.size() - 1); ++x) {
        for (int y = max(0, j - 1); y <= min(j + 1, grid[0].size() - 1); ++y) {
            if (!visited[x][y] && abs(x - i) + abs(y - j) == 1) {
                visited[x][y] = true;
                dfs(grid, visited, x, y, k - 1, path);
                visited[x][y] = false;
            }
        }
    }
    
    path.pop_back();
}