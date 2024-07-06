#include <vector>
#include <algorithm>

bool issame(std::vector<int> a, std::vector<int> b) {
    if (a.size() != b.size()) return false;
    for(int i = 0; i < a.size(); i++) {
        if (a[i] != b[b.size()-1-i]) return false;
    }
    return true;
}

int main() {
    std::vector<int> array({21, 14, 23, 11});
    sort_array(array);
    assert(issame(array, {11, 14, 21, 23}));
    return 0;
}