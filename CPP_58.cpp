vector<int> common(vector<int> l1, vector<int> l2) {
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());

    if(s1.size() == 0 || s2.size() == 0)
        throw runtime_error("Error: At least one of the vectors is empty.");

    set<int> resultIntersection; 
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(),
                      inserter(resultIntersection, resultIntersection.begin()));

    vector<int> result(resultIntersection.begin(), resultIntersection.end());
    return result;
}