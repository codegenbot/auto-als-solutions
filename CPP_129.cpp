#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> minPath(vector<vector<int>>& grid, int k) {
    int n = grid.size();
    vector<vector<int>> dp(n, vector<int>(n));
    for (int i = 0; i < n; ++i)
        dp[i][0] = grid[i][0];
    for (int j = 1; j < n; ++j)
        for (int i = 0; i < n; ++i)
            dp[i][j] = min({grid[i-1][j-1], grid[i][j-1], grid[i+1][j-1]} , {grid[i-1][j], grid[i][j], grid[i+1][j]} );
    vector<int> path;
    for (int i = 0; i < k; ++i) {
        int x = 0, y = 0;
        if(i==0){
            x=0,y=k-1;
        }else{
            for(int j = 0;j<n;++j){
                if(dp[0][j]<dp[x][y]){
                    x=j;
                    break;
                }
            }
            path.push_back(grid[x][y]);
            grid[x][y] = -1;
            y--;
            while(y>=0 && x==n-1) {
                for (int j = 0; j < n; ++j)
                    if (dp[0][j] < dp[j][y]) {
                        x = j;
                        break;
                    }
                path.push_back(grid[x][y]);
                grid[x][y] = -1;
                y--;
            }
        }
    }
    return path;
}

int main() {
    // Example usage:
    vector<vector<int>> grid = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int k = 3;
    vector<int> result = minPath(grid, k);
    for (int i : result) {
        cout << i << " ";
    }
    return 0;
}