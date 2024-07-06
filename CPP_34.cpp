```cpp
#include <algorithm>
#include <vector>

std::vector<int> unique(std::vector<int> l) {
    std::sort(l.begin(), l.end());
    auto result_end = std::unique(l.begin(), l.end());
    l.erase(result_end, l.end());
    return l;
}