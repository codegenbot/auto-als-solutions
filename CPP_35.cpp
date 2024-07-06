```cpp
#include <algorithm>
#include <cmath>

int maxAbsSum(int a[], int n) {
    if (n == 0)
        return 0;
    
    std::vector<int> l;
    for (int i = 0; i < n; i++) {
        l.push_back(a[i]);
    }
    
    return std::abs(*std::max_element(l.begin(), l.end()));
}