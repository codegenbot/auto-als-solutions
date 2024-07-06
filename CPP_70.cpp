#include <algorithm>
#include <vector>

bool issame(int x, int y) {
    return x == y;
}

std::vector<int> strange_sort_list(std::vector<int> lst) {
    std::vector<int> result;
    while (!lst.empty()) {
        int min_val = *min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(remove(lst.begin(), lst.end(), min_val), lst.end());
        
        if (!lst.empty()) {
            int max_val = *max_element(lst.begin(), lst.end());
            auto it = std::remove_if(lst.begin(), lst.end(), [max_val](int x) { return x == max_val; });
            lst.erase(it, lst.end());
            result.push_back(max_val);
        } else {
            result.push_back(*min_element(lst.begin(), lst.end()));
        }
    }
    return result;
}