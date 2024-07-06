```cpp
#include <vector>
#include <algorithm>

int smallest_change(std::vector<int> arr) {
    int n = arr.size();
    std::vector<std::vector<size_t>> dp(n, std::vector<size_t>(n));
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = 0;
    }
    
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            
            if (arr[i] == arr[j]) {
                dp[i][j].push_back(0);
            } else {
                size_t min_ops = INT_MAX;
                for (int k = i; k <= j; k++) {
                    size_t ops = 1 + (k-1 < 0 || i > 0 ? 0 : dp[i-1][k-1]) + (j >= n || j < n-1 ? 0 : dp[k+1][j]);
                    if (ops < min_ops) {
                        min_ops = ops;
                    }
                }
                dp[i][j].push_back(min_ops);
            }
        }
    }
    
    return *std::max_element(dp[0].begin(), dp[0].end());
}