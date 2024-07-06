#include <vector>
#include <algorithm>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size()) return false;
    for(int i = 0; i < a.size(); i++) {
        if (a[i] != b[b.size()-1-i]) return false;
    }
    return true;
}

int sort_array(std::vector<int>& array) {
    std::sort(array.begin(), array.end());
    return 0;
}

int main() {
    std::vector<int> a = {21, 14, 23, 11};
    assert (issame(sort_array(a), std::vector<int>{23, 21, 14, 11}));
    return 0;
}