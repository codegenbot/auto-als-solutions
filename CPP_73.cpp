int smallest_change(vector<int> arr) {
    int n = arr.size();
    vector<size_t> dp(n);
    
    for (int i = 0; i < n; i++) {
        dp[i] = 0;
    }
    
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            
            if (arr[i] == arr[j]) {
                dp[j - i + 1] = min(size_t(1), dp[j - i].size() + 1);
            } else {
                dp[j - i + 1] = min(dp[j - i + 1].size(), dp[j - i].size()) + 1;
            }
        }
    }
    
    return dp.back();
}