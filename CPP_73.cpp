#include <vector>
#include <algorithm>

int smallest_change(std::vector<int> arr) {
    int n = arr.size();
    std::vector<std::vector<size_t>> dp(n+1, std::vector<size_t>(n));

    for (int i = 0; i <= n; i++) {
        dp[i][i] = 0;
    }

    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;

            if (arr[i] == arr[j]) {
                size_t temp = dp[i+1][j-1].size() + 1;
                size_t min_len = dp[i+1][j].size();
                dp[i][j] = std::min(temp, min_len);
            } else {
                size_t min_len = *std::min_element(dp[i+1].begin(), dp[j].end()) + 1;
                dp[i][j] = min_len;
            }
        }
    }

    return dp[0][n-1].size();
}