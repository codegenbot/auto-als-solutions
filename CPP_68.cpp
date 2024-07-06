#include <vector>
#include <algorithm>

bool same(const std::vector<int>& a, const std::vector<int>& b) {
    return a == b;
}

std::vector<int> extract(std::vector<int> arr) {
    bool all_even = true;
    bool all_odd = true;

    for (int i : arr) {
        if (i % 2 != 0)
            all_even = false;
        else
            all_odd = false;
    }

    return all_even ? {arr[0]} : {};
}