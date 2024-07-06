#include <algorithm>
#include <cmath>

int largestAbsoluteValue(vector<int> l) {
    return *max_element(l.begin(), l.end()) >= 0 ? *max_element(l.begin(), l.end()) : -(*max_element(l.begin(), l.end()));
}