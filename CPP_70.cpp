void strange_sort_list(std::vector<int>& lst) {
    std::vector<int> result;
    #include <vector>
    bool issame(std::vector<int> a, std::vector<int> b) {
        return a == b;
    }
    while (!lst.empty()) {
        int min_val = *std::min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(std::remove_if(lst.begin(), lst.end(), [min_val](int i){ return i == min_val; }), lst.end());

        if (!lst.empty()) {
            int max_val = *std::max_element(lst.begin(), lst.end());
            std::vector<int> temp;
            for (int i : lst) {
                if (i != max_val) {
                    temp.push_back(i);
                }
            }
            result.insert(result.end(), temp.begin(), temp.end());
        } else {
            int min_val2 = *std::min_element(lst.begin(), lst.end());
            result.push_back(min_val2);
        }
    }
}