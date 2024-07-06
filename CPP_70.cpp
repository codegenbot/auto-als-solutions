#include <iostream>
#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

void strange_sort_list(std::vector<int>& lst) {
    std::vector<int> result;
    while (!lst.empty()) {
        int min_val = *std::min_element(lst.begin(), lst.end());
        result.push_back(min_val);
        lst.erase(std::remove(lst.begin(), lst.end(), min_val), lst.end());
    }
}

int main() {
    int v[] = {1, 1, 1, 1, 1};
    assert(issame(strange_sort_list(std::vector<int>(v, v + 1)) , std::vector<int>(v, v + 1)));
    return 0;
}