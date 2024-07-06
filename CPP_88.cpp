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
    assert(issame(std::vector<int>({-1, -1, 1, 2}), std::vector<int>({1, 2, -1, -1})));
    return 0;
}