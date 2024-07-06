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
                int min_len = dp[i+1][j-1].size();
            } else {
                int min_len = 1 + dp[i+1][j].size();
            }
            dp[i][j].push_back(min_len);
        }
    }
    
    return dp[0][n-1].back();
}