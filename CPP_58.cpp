```cpp
vector<int> common(vector<int> l1, vector<int> l2) {
    set<int> s1(l1.begin(), l1.end());
    set<int> s2(l2.begin(), l2.end());

    set<int> resultIntersection;
    set_difference(s1.begin(), s1.end(), s2.begin(), s2.end(),
                    inserter(resultIntersection, resultIntersection.begin()));

    vector<int> result;
    for (int i : resultIntersection) {
        if (count(l1.begin(), l1.end(), i) > 0 && count(l2.begin(), l2.end(), i) > 0)
            result.push_back(i);
    }
    return result;
}