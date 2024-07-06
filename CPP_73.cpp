#include <vector>
#include <size_t>

int smallest_change(std::vector<int> arr) {
    int n = arr.size();
    std::vector<std::vector<size_t>> dp(n, std::vector<size_t>(n));

    for (int i = 0; i < n; i++) {
        if (i == 0) {
            dp[i][i] = 1;
        } else if (arr[i] == arr[i-1]) {
            dp[i][i] = 1 + dp[i-1][i].size();
        } else {
            dp[i][i] = 2;
        }
    }

    int minChanges = dp[0][n-1];
    for (int i = 1; i < n; i++) {
        if (arr[i] == arr[i-1]) {
            size_t prevMinChanges = minChanges;
            minChanges = dp[i][i].size() + prevMinChanges;
        } else {
            minChanges = 2;
        }
    }

    return minChanges - 1;
}