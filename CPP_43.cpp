#include <vector>
#include <algorithm>

bool pairs_sum_to_zero(std::vector<int> l) {
    std::sort(l.begin(), l.end());
    for (int i = 0; i < l.size() - 1; ++i) {
        if (l[i] + l[i+1] == 0) return true;
    }
    for(int i = 0; i < l.size(); i++) {
        if(std::find(l.begin(), l.end(), -l[i]) != l.end()) {
            return true;
        }
    }
    return false;
}

int main() {
    assert(pairs_sum_to_zero({-3, 9, -1, 4, 2, 31}) == false);
    return 0;
}