#include <vector>
#include <algorithm>

bool check_arrays(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size()) return false;
    for(int i = 0; i < a.size(); i++) {
        if (a[i] != b[b.size()-1-i]) return false;
    }
    return true;
}

std::vector<int> sort_array(std::vector<int> array) { 
    std::sort(array.begin(), array.end());
    return array;
}

int main() {
    assert(check_arrays(sort_array({21, 14, 23, 11}), {23, 21, 14, 11}));
    return 0;
}