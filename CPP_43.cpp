#include <vector>
#include <algorithm>

bool pairs_sum_to_zero(std::vector<int> l) {
    std::sort(l.begin(), l.end());
    for (int i = 0; i < l.size() - 1; ++i) {
        j = l.size() - 1;
        while (j > i) {
            if (l[i] + l[j] == 0) return true;
            if (l[i] < l[j]) --j;
            else j--;
        }
    }
    return false;
}