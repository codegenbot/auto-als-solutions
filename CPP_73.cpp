#include <vector>
#include <algorithm>

int smallest_change(std::vector<int> arr) {
    int n = arr.size();
    std::vector<size_t> dp(n-1);
    
    for (int i = 0; i < n - 1; i++) {
        dp[i] = INT_MAX;
    }
    
    for (int i = 0; i < n - 1; i++) {
        if (arr[i] == arr[i+1]) {
            dp[i] = 0;
        } else {
            int min_ops = INT_MAX;
            for (int k = 0; k <= 1; k++) {
                size_t ops = 1 + (k==0 ? dp[i-1]:0) + (k==1?0:dp[i].size());
                if (ops < min_ops) {
                    min_ops = ops;
                }
            }
            dp[i] = min_ops;
        }
    }
    
    return *std::max_element(dp.begin(), dp.end())+1;
}