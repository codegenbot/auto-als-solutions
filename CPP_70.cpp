vector<int> strange_sort_list(vector<int> lst) {
    vector<int> result;
    while (!lst.empty()) {
        int min = *min_element(lst.begin(), lst.end());
        int max = *max_element(lst.begin(), lst.end());
        auto it_min = std::find(lst.begin(), lst.end(), min);
        auto it_max = std::find(lst.begin(), lst.end(), max);
        result.push_back(*it_min);
        lst.erase(it_min);
        if (!lst.empty()) {
            result.push_back(*it_max);
            lst.erase(it_max);
        }
    }
    return result;
}