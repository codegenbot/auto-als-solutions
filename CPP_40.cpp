#include <vector>
#include <algorithm>

using namespace std;

bool triples_sum_to_zero(vector<int> l) {
    set<int> s(l.begin(), l.end());
    for (auto i = s.begin(); i != s.end(); ++i) {
        int target = -(*i);
        auto left = s.begin();
        auto right = s.end();
        while (left < right) {
            int sum = *left + *right;
            if (sum == target) {
                return true;
            }
            else if (sum < target) {
                ++left;
            }
            else {
                --right;
            }
        }
    }
    return false;
}