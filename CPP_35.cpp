```cpp
#include <algorithm>
#include <cmath>

int maxAbsSum(vector<int> l) {
    return std::abs(*std::max_element(l.begin(), l.end()));
}