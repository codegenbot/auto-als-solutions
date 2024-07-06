#include <vector>
#include <algorithm>

int smallest_change(std::vector<int> arr) {
    int n = arr.size();
    std::vector<std::vector<int>> dp(n, std::vector<int>(n-1));
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = 0;
    }
    
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            
            if (arr[i] == arr[j]) {
                dp[i][j] = dp[i+1][j-1].size();
            } else {
                int min_ops = INT_MAX;
                for (int k = i; k <= j; k++) {
                    int ops = 1 + dp[i][k-1].size() + dp[k+1][j].size();
                    if (ops < min_ops) {
                        min_ops = ops;
                    }
                }
                dp[i][j] = min_ops;
            }
        }
    }
    
    return *std::max_element(dp[0].begin(), dp[0].end());
}