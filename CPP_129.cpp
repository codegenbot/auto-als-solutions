```cpp
#include <vector>
#include <utility>

int pathFinder(std::vector<std::vector<char>>& grid, int x, int y, std::vector<std::pair<int, int>>& path) {
    if (grid.empty() || grid[0].empty()) return -1;
    
    for(int i = 0; i < grid.size(); i++) {
        for(int j = 0; j < grid[i].size(); j++) {
            if(grid[i][j] == 'S') {
                grid[i][j] = '#';
                dfs(grid, x, y, path);
                grid[i][j] = 'S';
                return 1;
            }
        }
    }
    
    return 0;
}

void dfs(std::vector<std::vector<char>>& grid, int i, int j, std::vector<std::pair<int, int>>& path) {
    if(i < 0 || i >= grid.size() || j < 0 || j >= grid[i].size()) 
        return;
    
    if(grid[i][j] == '#') {
        grid[i][j] = 'P';
        path.push_back({i, j});
        dfs(grid, i+1, j, path);
        dfs(grid, i-1, j, path);
        dfs(grid, i, j+1, path);
        dfs(grid, i, j-1, path);
    }
}