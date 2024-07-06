#include <iostream>
#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

void strange_sort_list(std::vector<int>& lst) {
    std::sort(lst.begin(), lst.end());
}

int main() {
    std::vector<int> input = {1, 1, 1, 1, 1};
    
    strange_sort_list(input);
    return 0;
}