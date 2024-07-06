#include <vector>
using namespace std;

vector<int> minPath(vector<vector<int>> grid, int k) {
    int n = grid.size();
    vector<vector<bool>> visited(n, vector<bool>(n));
    vector<int> res;
    
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(visited[i][j]) continue;
            vector<int> path = dfs(grid, i, j, k, visited);
            if(path.size() > 0 && (res.empty() || path < res)){
                res = path;
            }
        }
    }
    
    return res;
}

vector<int> dfs(vector<vector<int>>& grid, int x, int y, int k, vector<vector<bool>>& visited) {
    vector<int> path;
    for(int i=0; i<k; i++){
        path.push_back(grid[x][y]);
        if(i == k-1) return path;
        vector<pair<int, int>> neighbors = {{x-1, y}, {x+1, y}, {x, y-1}, {x, y+1}};
        for(auto& neighbor : neighbors){
            int nx = neighbor.first, ny = neighbor.second;
            if(nx >= 0 && nx < grid.size() && ny >= 0 && ny < grid[0].size() && !visited[nx][ny]){
                visited[nx][ny] = true;
                x = nx; y = ny;
                break;
            }
        }
    }
    
    return path;
}