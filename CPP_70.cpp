vector<int> strange_sort_vector(vector<int> lst) {
    vector<int> result;
    if (lst.empty()) return result;

    auto min_max = [&]() -> pair<int, int> {
        int min_val = *min_element(lst.begin(), lst.end());
        int max_val = *max_element(lst.begin(), lst.end());
        return {min_val, max_val};
    };

    while (!lst.empty()) {
        auto [min_val, max_val] = min_max();
        result.push_back(min_val);
        lst.erase(std::remove_if(lst.begin(), lst.end(),
            [&](int val) { return val == min_val; }), lst.end());
        if (!lst.empty())
            result.push_back(max_val);
        lst.erase(std::remove_if(lst.begin(), lst.end(),
            [&](int val) { return val == max_val; }), lst.end());
    }

    return result;
}