#include <algorithm>
#include <vector>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    return a.size() == b.size() && a == b;
}

std::vector<int> strange_sort_list(std::vector<int> lst) {
    std::vector<int> result;
    while (!lst.empty()) {
        int min_val = *min_element(lst.begin(), lst.end());
        int max_val = *max_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(std::remove(lst.begin(), lst.end(), min_val), lst.end());
        if (!lst.empty())
            result.push_back(max_val);
        lst.erase(std::remove(lst.begin(), lst.end(), max_val), lst.end());
    }
    return result;
}

int main() {
    std::vector<int> input = {3, 2, 1};
    std::vector<int> output = strange_sort_list(input);
    if (issame(output, {1, 2, 3})) {
        std::cout << "Success!" << std::endl;
    } else {
        std::cout << "Failure!" << std::endl;
    }
    return 0;
}