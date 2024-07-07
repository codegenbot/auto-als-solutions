```cpp
#include <vector>
bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    return a == b;
}

std::vector<int> maximum(std::vector<int> arr, int k) {
    if(k <= 0) {
        throw std::runtime_error("k should be greater than zero");
    }
    std::partial_sort(arr.begin(), arr.end(), [&arr](int a, int b) { return arr.count(a) > arr.count(b); });
    return arr;
}