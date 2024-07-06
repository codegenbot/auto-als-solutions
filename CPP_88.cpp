#include <iostream>
#include <vector>
#include <algorithm>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size()) return false;
    for(int i = 0; i < a.size(); i++) {
        if (a[i] != b[b.size()-1-i]) return false;
    }
    return true;
}

int main() {
    assert(issame(std::vector<int>({21, 14, 23, 11}), std::vector<int>({23, 21, 14, 11})) );
    return 0;
}