int smallest_change(std::vector<int> arr) {
    int n = arr.size();
    std::vector<std::vector<uint64_t>> dp(n, std::vector<uint64_t>(n-1));

    for (int i = 0; i < n; i++) {
        dp[i][i] = 0;
    }

    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;

            if (arr[i] == arr[j]) {
                uint64_t min_change = dp[i+1][j-1].size();
                for (uint64_t k : dp[i+1][j-1]) {
                    min_change += k;
                }
                dp[i][j].push_back(min_change);
            } else {
                if (i == 0) {
                    dp[i][j].push_back(1 + dp[i][j-1].size());
                } else if (j == n - 1) {
                    dp[i][j].push_back(1 + dp[i+1][j].size());
                } else {
                    uint64_t left = 1 + dp[i][j-1].size();
                    uint64_t right = 1 + dp[i+1][j].size();
                    for (uint64_t k : dp[i][j-1]) {
                        left += k;
                    }
                    for (uint64_t k : dp[i+1][j]) {
                        right += k;
                    }
                    dp[i][j].push_back(std::min(left, right));
                }
            }
        }
    }

    return dp[0][n-1].size();
}