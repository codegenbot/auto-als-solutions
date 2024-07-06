#include <stdio.h>
#include <vector>
using namespace std;

vector<int> minPath(vector<vector<int>> grid, int k) {
    vector<vector<int>> dp(grid.size() + 1, vector<int>(grid[0].size() + 1, INT_MAX));
    dp[0][0] = 0;
    
    for (int i = 0; i < grid.size(); ++i) {
        for (int j = 0; j < grid[i].size(); ++j) {
            if (i > 0) dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1;
            if (j > 0) dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1;
            
            for (int x : {i - 1, i, j - 1, j}) {
                if (x < 0 || x >= grid.size() || !grid[x].empty()) {
                    int val = dp[x][min(j, grid[0].size()-1)];
                    if (val < INT_MAX) break;
                }
            }
        }
    }
    
    vector<int> res(k + 1);
    int minSum = INT_MAX, prevI = -1, prevJ = -1;
    
    for (int i = grid.size() - 1; i >= 0; --i) {
        for (int j = grid[i].size() - 1; j >= 0; --j) {
            if (dp[i][j] < minSum) {
                minSum = dp[i][j];
                prevI = i;
                prevJ = j;
            }
        }
    }
    
    int currVal = grid[prevI][prevJ], cnt = 1, idx = 0;
    
    while (cnt <= k) {
        res[idx++] = currVal;
        if (prevI > 0 && dp[prevI-1][prevJ] == minSum - 1) {
            prevI--;
        } else if (prevJ > 0 && dp[prevI][prevJ-1] == minSum - 1) {
            prevJ--;
        }
        minSum--;
    }
    
    return res;
}