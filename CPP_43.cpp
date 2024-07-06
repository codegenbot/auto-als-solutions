#include <vector>
#include <algorithm>

bool pairs_sum_to_zero(std::vector<int> l) {
    std::sort(l.begin(), l.end());
    for (int i = 0; i < l.size() - 1; ++i) {
        if (std::abs(l[i]) + l[i] == 0) return true;
        int j = i + 1;
        while (j < l.size() && l[j] <= std::abs(l[i])) {
            if (l[i] + l[j] == 0) return true;
            ++j;
        }
    }
    for (int i = 0; i < l.size(); ++i) {
        if (std::abs(l[i]) * 2 == l[i]) return true;
    }
    return false;
}

int main() {
    std::vector<int> numbers = {-3, 9, -1, 4, 2, 31};
    bool result = pairs_sum_to_zero(numbers);
    assert(result == false);
    return 0;
}