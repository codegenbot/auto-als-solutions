vector<int> strange_sort_vector(vector<int> lst) {
    vector<int> result;
    if (lst.empty()) return result;

    std::sort(lst.begin(), lst.end());
    bool isMin = true;
    for (int num : lst) {
        if (isMin) {
            result.push_back(*std::min_element(lst.begin(), lst.end()));
            lst.erase(std::remove(lst.begin(), lst.end(), *std::min_element(lst.begin(), lst.end())), lst.end());
        } else {
            result.push_back(*std::max_element(lst.begin(), lst.end()));
            lst.erase(std::remove(lst.begin(), lst.end(), *std::max_element(lst.begin(), lst.end())), lst.end());
        }
        isMin = !isMin;
    }

    return result;
}