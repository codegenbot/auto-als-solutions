#include <algorithm>
#include <cmath>

int maxAbsolute(int l[]) {
    return std::abs(*std::max_element(l, l + sizeof(int) / sizeof(int)));
}