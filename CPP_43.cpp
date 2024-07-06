#include <vector>
#include <set>

bool pairs_sum_to_zero(const vector<int>& l) {
    set<int> s(l.begin(), l.end());
    for (int x : s) {
        int target = -x;
        if (s.find(target) != s.end() && target != x) {
            return true;
        }
    }
    return false;
}