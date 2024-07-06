```
#include <vector>
#include <set>
#include <algorithm>

bool issame(const std::vector<int>& v1, const std::vector<int>& v2) {
    if (v1.size() != v2.size()) return false;
    for (int i = 0; i < v1.size(); ++i) {
        if (v1[i] != v2[i]) return false;
    }
    return true;
}

std::vector<int> common(std::vector<int> l1, std::vector<int> l2) {
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());
    set<int> intersection;

    if (!issame(s1.begin(), s1.end(), s2.begin(), s2.end())) {
        set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
            inserter(intersection, intersection.begin()));
    }
    vector<int> result(intersection.begin(), intersection.end());
    return result;
}