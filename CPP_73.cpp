#include <vector>
#include <algorithm>

using namespace std;

int smallest_change(vector<int> arr) {
    int n = arr.size();
    vector<vector<size_t>> dp(n, vector<size_t>(n));
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = 0;
    }
    
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            
            if (arr[i] == arr[j]) {
                dp[i][j].resize(dp[i+1][j-1].size() + 1, 0);
            } else {
                dp[i][j].resize(min(size_t(1), size_t(dp[i+1][j-1].size())) + 1);
                dp[i][j][0] = min(size_t(1), size_t(dp[i+1][j-1].size())) + 1;
            }
        }
    }
    
    return *max_element(dp[0].begin(), dp[0].end());
}