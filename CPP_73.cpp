#include <iostream>
#include <vector>

int smallest_change(std::vector<int>& coins) {
    int n = coins.size();
    std::vector<std::vector<size_t>> dp(n, std::vector<size_t>(n-1));
    
    for (int i = 0; i < n; i++) {
        dp[i][i] = 0;
    }
    
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            
            if (coins[i] == coins[j]) {
                dp[i][j].push_back(dp[i+1][j-1].size());
            } else {
                dp[i][j].push_back(1 + std::max(dp[i+1][j], dp[i][j-1]).size());
            }
        }
    }
    
    return dp[0][n-1].size();
}

int main() {
    int n;
    std::cout << "Enter number of coins: ";
    std::cin >> n;
    
    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cout << "Coin " << i + 1 << ": ";
        int coin;
        std::cin >> coin;
        arr[i] = coin;
    }
    
    std::cout << "Minimum number of changes needed: " << smallest_change(arr) << std::endl;
    return 0;
}