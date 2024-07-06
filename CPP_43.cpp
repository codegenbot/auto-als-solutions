#include <vector>
using namespace std;

bool pairs_sum_to_zero(vector<int> l) {
    unordered_set<int> s(l.begin(), l.end());
    for (auto i : s) {
        if (s.count(-i)) return true;
    }
    return false;
}