#include <algorithm>
int maxElement(vector<int> l) {
    return *std::max_element(l.begin(), l.end());
}