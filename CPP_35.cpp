#include <algorithm>

int findMax(std::vector<int> l) {
    return *std::max_element(l.begin(), l.end());
}