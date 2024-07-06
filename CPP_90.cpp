```cpp
#include <vector>
#include <algorithm>

int next_smallest(std::vector<int> vec) {
    if (vec.empty()) return 0; 
    int result = INT_MAX;
    for (int i = 1; i < vec.size(); i++) {
        if (vec[i] > vec[0]) {
            result = std::min(result, vec[i]);
        }
    }
    return result == INT_MAX ? 0 : result;
}