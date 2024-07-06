Here is the solution:

int next_smallest(vector<int> lst) {
    vector<int> v(lst);
    sort(v.begin(), v.end());
    if (v.size() < 2) return -1;
    int idx = distance(v.begin(), find(v.begin(), v.end(), v[1]));
    return *idx == v[0] ? -1 : v[1];
}