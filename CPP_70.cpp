#include <iostream>
#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

void strange_sort_list(std::vector<int>& lst) {
    std::vector<int> result;
    int min_val = 0;
    while (!lst.empty()) {
        min_val = *std::min_element(lst.begin(), lst.end());
        for (int i : lst) {
            if (i == min_val) {
                lst.erase(std::remove(lst.begin(), lst.end(), i), lst.end());
                break;
            }
        }
        result.push_back(min_val);
    }
}

int main() {
    int v[] = {1, 1, 1, 1, 1};
    assert(issame(strange_sort_list(std::vector<int>(v, v + 1)) , std::vector<int>(v, v + 1)));
    return 0;
}