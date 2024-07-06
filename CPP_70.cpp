#include <algorithm>
#include <vector>

std::vector<int> strange_sort_vector(const std::vector<int>& lst) {
    if (lst.empty()) {
        return {};
    }

    std::vector<int> result;

    while (!lst.empty()) {
        int minVal = *min_element(lst.begin(), lst.end());
        result.push_back(minVal);

        auto it = lst.begin();
        advance(it, distance(lst.begin(), find(it, lst.end(), minVal)) - 1);
        lst.erase(it);

        if (!lst.empty()) {
            int maxVal = *max_element(lst.begin(), lst.end());
            result.push_back(maxVal);
            lst.erase(find(lst.begin(), lst.end(), maxVal) - lst.begin());
        }
    }

    return result;
}