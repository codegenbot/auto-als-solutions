```cpp
#include <vector>
#include <algorithm>

bool move_one_ball(std::vector<int> arr) {
    int n = arr.size();
    if (n == 0) return true;

    for (int i = 1; i < n; ++i) {
        if (arr[i] < *arr.begin()) return false;
    }

    return true;
}