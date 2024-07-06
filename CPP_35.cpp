#include <algorithm>

int findMax(vector<int> l) {
    return *std::max_element(l.begin(), l.end());
}