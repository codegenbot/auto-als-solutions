#include <algorithm>

vector<int> unique(vector<int> l) {
    vector<int> result(l.begin(), unique_copy(l.begin(), l.end()).end());
    return result;
}

vector<int>::iterator unique_copy(iterator start, iterator end) {
    sort(start, end);
    iterator i = start;
    for (++i; i != end; ++i) {
        if (*i == *(i - 1)) {
            *i = INT_MIN;
        }
    }
    for (iterator j = start; j != end; ++j) {
        if (*j == INT_MIN) continue;
        *j = *(i - 1);
    }
    return i;
}