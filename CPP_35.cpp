```cpp
int maxElement(vector<int> l) {
    include <algorithm>
    return *max_element(l.begin(), l.end());
}