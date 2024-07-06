#include <vector>
#include <algorithm>

using namespace std;

int smallest_change(vector<int> arr) {
    int n = arr.size();
    vector<vector<int>> dp(n, vector<int>(n));
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = 0;
    }
    
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            
            if (arr[i] == arr[j]) {
                size_t sz = dp[i+1][j-1].size();
                if (sz == 0) {
                    sz = 1;
                }
                dp[i].resize(j - i + 1);
                dp[i][j - i] = sz;
            } else {
                size_t sz = dp[i+1][j-1].size();
                if (sz == 0) {
                    sz = 1;
                }
                dp[i].resize(j - i + 1);
                dp[i][j - i] = min(size_t(1), sz) + 1;
            }
        }
    }
    
    return dp[0].size() - 1;
}