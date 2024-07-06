```cpp
#include <vector>
#include <algorithm>

int main() {
    assert(pairs_sum_to_zero({-3, 9, -1, 4, 2, 31}) == false);
    return 0;
}

bool pairs_sum_to_zero(std::vector<int> l) {
    std::sort(l.begin(), l.end());
    for (int i = 0; i < l.size(); ++i) {
        int target = -l[i];
        int j = i + 1;
        while (j < l.size()) {
            if (std::abs(l[j]) == target) return true;
            if (l[j] > target) break;
            ++j;
        }
    }
    return false;
}