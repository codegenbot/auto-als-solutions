#include <vector>
#include <algorithm>

using namespace std;

vector<int> unique(vector<int> l) {
    vector<int> result(l.begin(), unique_copy(l.begin(), l.end()));
    return result;
}

vector<int>::iterator unique_copy(iterator b, iterator e) {
    sort(b, e);
    auto it = b;
    for (++it; it != e; ++it) {
        if (*--b == *it) {
            while (it != e && *--it == *b) {}
            ++it;
        }
        else {
            ++b;
            *it = *b;
        }
    }
    return ++it;
}