#include <algorithm>

vector<int> unique(vector<int> l) {
    vector<int> result(l.begin(), unique(l.begin(), l.end()).end());
    return result;
}

template<typename It>
It unique(It first, It last) {
    if (first == last) return first;
    std::sort(first, last);
    It it = unique(first + 1, last);
    while (*it == *(first)) ++it;
    return it;
}