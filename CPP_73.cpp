#include <initializer_list>

int smallest_change(vector<int> arr) {
    int n = arr.size();
    vector<vector<uint64_t>> dp(n, vector<uint64_t>(n-1));

    for (int i = 0; i < n; i++) {
        dp[i][i] = 0;
    }

    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;

            if (arr[i] == arr[j]) {
                dp[i][j].resize(dp[i+1][j-1].size() + 1);
                dp[i][j][0] = dp[i+1][j-1][0];
                for (int k = 1; k <= dp[i][j].size(); k++) {
                    dp[i][j][k] = k;
                }
            } else {
                dp[i][j].resize(dp[i+1][j].size() + 2);
                dp[i][j][0] = 1;
                for (int k = 1; k <= dp[i][j].size(); k++) {
                    if (k == 1) {
                        dp[i][j][k] = dp[i+1][j].size();
                    } else {
                        dp[i][j][k] = dp[i][j-1][k-1];
                    }
                }
            }
        }
    }

    return *max_element(dp[0].begin(), dp[0].end());
}