#include <vector>
#include <algorithm>

using namespace std;

bool triples_sum_to_zero(vector<int> l) {
    set<int> s(l.begin(), l.end());
    for (int i : s) {
        int j = -i;
        if (j != i && find(s.begin(), s.end(), j) != s.end()) {
            int k = -(i + j);
            if (k != i && k != j && find(s.begin(), s.end(), k) != s.end())
                return true;
        }
    }
    return false;
}