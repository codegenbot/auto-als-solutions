#include <algorithm>
#include <vector>
using namespace std;

vector<int> minPath(vector<vector<int>> grid, int k) {
    vector<vector<int>> dp(grid.size(), vector<int>(grid[0].size()));
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (i == 0 && j == 0) {
                dp[i][j] = grid[i][j];
            } else if (i > 0) {
                dp[i][j] = min({dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]}) + grid[i][j];
            } else if (j > 0) {
                dp[i][j] = min({dp[i][j-1], dp[i-1][j-1], dp[i+1][j-1]}) + grid[i][j];
            } else {
                dp[i][j] = min({dp[i-1][j], dp[i-1][j+1]}) + grid[i][j];
            }
        }
    }

    vector<int> result;
    int i = 0, j = 0;
    for (int l = 1; l <= k; l++) {
        result.push_back(grid[i][j]);
        if (i > 0 && j > 0) {
            if (dp[i-1][j] < dp[i][j-1] && dp[i-1][j] < dp[i+1][j]) i--;
            else if (dp[i][j-1] < dp[i-1][j] && dp[i][j-1] < dp[i+1][j]) j--;
            else i++;
        } else if (i > 0) {
            i--;
        } else {
            j--;
        }
    }

    return result;
}