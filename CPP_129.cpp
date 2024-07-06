#include <iostream>
#include <vector>
using namespace std;

vector<int> minPath(vector<vector<int>>& grid, int k) {
    vector<vector<int>> dp(grid.size(), vector<int>(grid[0].size()));
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = grid[i][j];
            } else {
                int minVal = INT_MAX;
                if (grid[i-1][j] < minVal) minVal = grid[i-1][j];
                if (grid[i][j-1] < minVal) minVal = grid[i][j-1];
                dp[i][j] = minVal;
            }
        }
    }

    vector<int> res;
    int i = 0, j = 0;
    for (int l = 0; l < k; l++) {
        res.push_back(grid[i][j]);
        if (i == 0) {
            j++;
        } else if (j == 0) {
            i--;
        } else if (grid[i-1][j] <= grid[i][j-1]) {
            i--;
        } else {
            j--;
        }
    }

    return res;
}

int main() {
    vector<vector<int>> grid = {{1,2,3}, {4,5,6}, {7,8,9}};
    int k = 3;
    vector<int> result = minPath(grid, k);
    for (int i : result) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}