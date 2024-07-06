#include <vector>
int smallest_change(std::vector<int> arr) {
    int n = arr.size();
    std::vector<std::vector<uint64_t>> dp(n, std::vector<uint64_t>(n));
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = 0;
    }
    
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            
            if (arr[i] == arr[j]) {
                dp[i][j].push_back(0);
                if (i+1 <= j) {
                    for (int k = 0; k < dp[i+1][j].size(); k++) {
                        dp[i][j].push_back(dp[i+1][j][k]);
                    }
                }
            } else {
                if (i+1 <= j) {
                    dp[i][j].push_back(1 + dp[i+1][j].size());
                } else {
                    dp[i][j].clear();
                    if (i+1 <= j) {
                        for (int k = 0; k < dp[i+1][j].size(); k++) {
                            dp[i][j].push_back(1 + dp[i+1][j][k]);
                        }
                    } else {
                        dp[i][j].push_back(1);
                    }
                }
            }
        }
    }
    
    return dp[0][n-1].size();
}