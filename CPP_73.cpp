int smallest_change(std::vector<int> arr) {
    int n = arr.size();
    std::vector<std::vector<size_t>> dp(n, std::vector<size_t>(n-1));
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = 0;
    }
    
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            
            if (arr[i] == arr[j]) {
                dp[i][j].push_back(dp[i+1][j-1].size());
            } else {
                dp[i][j].push_back(1 + dp[i+1][j].size());
            }
        }
    }
    
    return dp[0][n-1].size();
}