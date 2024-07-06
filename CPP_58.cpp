bool issame(vector<int> l1, vector<int> l2) {
    if (l1.size() != l2.size()) return false;
    for (int i = 0; i < l1.size(); i++) {
        if (l1[i] != l2[i]) return false;
    }
    return true;
}

vector<int> common(vector<int> l1, vector<int> l2) {
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());
    set<int> intersection;
    
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
        inserter(intersection, intersection.begin()));
    
    vector<int> result(intersection.begin(), intersection.end());
    return result;
}