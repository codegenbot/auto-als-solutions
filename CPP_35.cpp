```cpp
#include <algorithm>
#include <cmath>

int max_abs_value(const std::vector<int>& l) {
    return std::abs(*std::max_element(l.begin(), l.end()));
}