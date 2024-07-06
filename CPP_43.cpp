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
    for(int i = 0; i < l.size(); i++) {
        if(std::find(l.begin(), l.end(), -std::abs(l[i])) != l.end()) {
            return true;
        }
    }
    return false;
}

int main() {
    assert(pairs_sum_to_zero({-3, 9, -1, 4, 2, 31}) == false);
    return 0;
}