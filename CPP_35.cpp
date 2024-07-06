#include <algorithm>
#include <cmath>

int maxAbsSum(int l[], int n) {
    std::vector<int> v(l, l+n);
    return std::abs(*std::max_element(v.begin(), v.end()));
}