#include <algorithm>
#include <vector>

int findMaxElement(const std::vector<int>& l) {
    return *std::max_element(l.begin(), l.end());
}