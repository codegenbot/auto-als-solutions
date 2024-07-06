#include <vector>
#include <set>

bool issame(const std::vector<int>& l1, const std::vector<int>& l2) {
    if (l1.size() != l2.size()) return false;
    for (int i = 0; i < l1.size(); ++i)
        if (l1[i] != l2[i]) return false;
    return true;
}

std::vector<int> common(std::vector<int> l1, std::vector<int> l2) {
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());
    set<int> intersection;

    if (issame(s1.begin(), s1.end(), s2.begin(), s2.end())) {
        vector<int> result;
        for (auto it = s1.begin(); it != s1.end(); ++it)
            if (count(s2.begin(), s2.end(), *it)) result.push_back(*it);
        return result;
    }

    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
        inserter(intersection, intersection.begin()));
    
    vector<int> result(intersection.begin(), intersection.end());
    return result;
}