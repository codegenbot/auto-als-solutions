int smallest_change(vector<int> arr) {
    int n = arr.size();
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = true;
    }
    
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i < n - len + 1; i++) {
            int j = i + len - 1;
            if (arr[i] == arr[j]) {
                dp[i][j] = true;
            } else {
                dp[i][j] = false;
                for (int k = i; k <= j; k++) {
                    if (dp[i][k-1] && dp[k+1][j]) {
                        dp[i][j] = true;
                        break;
                    }
                }
            }
        }
    }
    
    int changes = 0;
    for (int i = 0, j = n - 1; i < j; ) {
        if (!dp[i][j]) {
            if (arr[i] != arr[j]) {
                if (arr[i] == arr[j-1]) {
                    j--;
                } else if (arr[j] == arr[i+1]) {
                    i++;
                } else {
                    changes++;
                    break;
                }
            } else {
                changes++;
                break;
            }
        }
        if (dp[i][j]) {
            i++;
            j--;
        }
    }
    
    return changes;
}