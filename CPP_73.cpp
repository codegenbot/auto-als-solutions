int smallest_change(vector<int> arr) {
    int n = arr.size();
    vector<vector<bool>> dp(n, vector<bool>(n));
    
    for (int i = 0; i < n; ++i)
        dp[i][i] = true;
    
    for (int length = 2; length <= n; ++length) {
        for (int i = 0; i < n - length + 1; ++i) {
            int j = i + length - 1;
            if (arr[i] == arr[j])
                dp[i][j] = true;
            else
                dp[i][j] = false;
            for (int k = i + 1; k < j; ++k)
                if (dp[i][k] && dp[k][j])
                    dp[i][j] = true;
        }
    }
    
    int changes = 0;
    for (int i = 0; i < n - 1; ++i) {
        if (!dp[0][n - 1]) {
            int j = i + 1;
            while (j <= n - 2 && !dp[0][n - 1])
                j++;
            changes += j - i;
            break;
        }
    }
    
    return changes;
}