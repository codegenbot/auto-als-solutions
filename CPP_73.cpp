Here is the solution:

int smallest_change(vector<int> arr) {
    int n = arr.size();
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    
    for (int i = 0; i < n; i++) {
        for (int j = i; j >= 0; j--) {
            if (i == j)
                dp[j][j] = true;
            else if (arr[i] == arr[j])
                dp[j][i] = dp[i + 1][j - 1];
            else
                dp[j][i] = false;
        }
    }
    
    int res = n;
    for (int i = 0; i < n; i++) {
        if (!dp[0][i]) {
            res = i;
            break;
        }
    }
    
    return res;
}