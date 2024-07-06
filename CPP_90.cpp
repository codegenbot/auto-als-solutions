Here is the completed code:

#include <vector>
#include <algorithm>

using namespace std;

int next_smallest(vector<int> lst) {
    if (lst.empty()) return -1; // Return None
    vector<int> v(lst);
    sort(v.begin(), v.end());
    int res = -1;
    for (int i = 0; i < v.size() - 1; i++) {
        if (v[i] != v[i + 1]) {
            return v[i + 1];
        }
    }
    return res;
}