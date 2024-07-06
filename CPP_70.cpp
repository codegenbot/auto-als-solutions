#include <iostream>
#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

void strange_sort_list(std::vector<int>& lst) {
    std::sort(lst.begin(), lst.end());
    int min_val = *std::min_element(lst.begin(), lst.end());
    for (int i : lst) {
        if (i != min_val) {
            result.push_back(i);
        }
    }
}

int main() {
    std::vector<int> input = {1, 1, 1, 1, 1};
    strange_sort_list(input);
    return 0;
}