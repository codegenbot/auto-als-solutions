#include <vector>
#include <algorithm>

using namespace std;

bool triples_sum_to_zero(vector<int> l) {
    set<int> s(l.begin(), l.end());
    for (int i = 0; i < s.size(); ++i) {
        int target = -s[i];
        bool found = false;
        for (int j = i + 1; j < s.size() && !found; ++j) {
            if (target - s[j] > 0 || target - s[j] == s[i]) continue;
            found = true;
            for (int k = j + 1; k < s.size(); ++k) {
                if (s[i] + s[j] + s[k] == 0) return true;
            }
        }
    }
    return false;
}