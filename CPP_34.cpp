#include <vector>
#include <algorithm>

using namespace std;

vector<int> unique(vector<int> l) {
    vector<int> result(l.begin(), unique_copy(l.begin(), l.end()).end());
    return result;
}

vector<int>::iterator unique_copy(iterator b, iterator e) {
    unordered_set<int> s(b, e);
    for (auto it = b; it != e; ++it) {
        *it = move(*s.find(*it));
    }
    return e;
}