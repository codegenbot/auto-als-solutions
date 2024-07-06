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
                dp[i][j] = dp[i+1][j-1];
            } else {
                dp[i][j] = min(size_t(1), dp[i+1][j-1]) + 1;
            }
        }
    }
    
    return *max_element(dp[0].begin(), dp[0].end());
}