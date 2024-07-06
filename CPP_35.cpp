```cpp
#include <algorithm>
#include <cmath>

int myMaximumNumber(int n) {
    int l[n];
    for (int i = 0; i < n; i++) {
        cin >> l[i];
    }
    return std::abs(*std::max_element(std::begin(l), std::end(l)));
}