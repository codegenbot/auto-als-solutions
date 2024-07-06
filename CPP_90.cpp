int next_smallest(vector<int> lst) {
    if (lst.empty()) return 0; 
    sort(lst.begin(), lst.end());
    for (int i = 1; i < lst.size(); i++) {
        if (lst[i] != lst[0]) {
            return lst[i];
        }
    }
    return 0; 
}