```cpp
#include <algorithm>

int findMax(int n, vector<int> l) {
    return *std::max_element(l.begin(), l.end());
}