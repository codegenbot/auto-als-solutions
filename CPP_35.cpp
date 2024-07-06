#include <algorithm>

int maxVal(vector<int> &l) {
    return *std::max_element(l.begin(), l.end());
}