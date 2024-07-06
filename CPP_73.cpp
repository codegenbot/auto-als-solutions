Here is the completed code:

```cpp
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
                    if (!dp[i][k-1] || !dp[k+1][j]) {
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
            changes++;
            if (arr[i] == arr[j-1]) {
                i++;
            } else if (arr[i+1] == arr[j]) {
                j--;
            } else {
                i++;
                j--;
            }
        } else {
            i++;
            j--;
        }
    }
    
    return changes;
}