#include <iostream>
#include <vector>
#include <algorithm>

int next_smallest(std::vector<int> lst) {
    if (lst.empty()) return -1; 
    std::vector<int> sorted = lst;
    std::sort(sorted.begin(), sorted.end());
    auto it = std::upper_bound(sorted.begin(), sorted.end(), sorted[0]);
    if (it == sorted.end()) return -1; 
    return *std::prev(it);
}

int main() {
    assert(next_smallest({-35, 34, 12, -45}) == -35);
    return 0;
}