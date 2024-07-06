void strange_sort_list(std::vector<int>& lst) {
    std::vector<int> result = lst;
    int min_val = 0;
    while (!result.empty()) {
        min_val = *std::min_element(result.begin(), result.end());
        for (int i : result) {
            if (i == min_val) {
                result.erase(std::remove(result.begin(), result.end(), i), result.end());
                break;
            }
        }
        std::cout << min_val << " ";
    }
    std::cout << "\n";
}