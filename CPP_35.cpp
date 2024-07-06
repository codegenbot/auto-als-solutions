```cpp
#include <algorithm>
#include <cmath>

int maximumSumSubarray(int k, int n) {
    if (k > n) 
        return 0;
    std::vector<int> l;
    for (int i = 1; i <= k; ++i) {
        int x;
        std::cin >> x;
        l.push_back(x);
    }
    return *std::max_element(l.begin(), l.end());
}