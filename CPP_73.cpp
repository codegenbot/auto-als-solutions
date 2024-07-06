#include <vector>
#include <cstdint>
#include <initializer_list>

int smallest_change(vector<int> arr) {
    int n = arr.size();
    vector<vector<uint64_t>> dp(n, vector<uint64_t>(n-1));
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = 0;
    }
    
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            
            if (arr[i] == arr[j]) {
                int count = dp[i+1][j-1].size();
                dp[i][j].push_back(count);
            } else {
                int count = 1 + dp[i+1][j].size();
                dp[i][j].push_back(count);
            }
        }
    }
    
    return dp[0][n-1].size();
}