vector<int> strange_sort_list(vector<int> lst) {
    vector<int> result;
    while (!lst.empty()) {
        int min_val = *min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        auto it = lst.begin();
        advance(it, distance(lst.begin(), find_if(lst.begin(), lst.end(),
            [min_val](int val) { return val == min_val; })));
        lst.erase(it);
    }
    return result;
}