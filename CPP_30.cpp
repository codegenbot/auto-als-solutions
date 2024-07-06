#include <vector>
#include <algorithm>

bool issame(vector<float> l1, vector<float> l2) {
    if (l1.size() != l2.size()) return false;
    for (float num : l1) {
        if (!std::count(l2.begin(), l2.end(), num)) return false;
    }
    return true;
}

int main() {
    assert(issame(get_positive({}), {}));