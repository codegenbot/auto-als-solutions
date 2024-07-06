vector<int> common(vector<int> l1, vector<int> l2) {
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());

    set<int> resultIntersection;
    if(s1.empty() || s2.empty()) {
        throw runtime_error("Both lists must not be empty");
    }
    
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                      inserter(resultIntersection, resultIntersection.begin()));

    vector<int> result(resultIntersection.begin(), resultIntersection.end());
    return result;
}