#include <vector>
#include <algorithm>

bool issame(vector<float> l1, vector<float> l2) {
    if (l1.size() != l2.size()) {
        return false;
    }
    for (size_t i = 0; i < l1.size(); ++i) {
        if (std::abs(l1[i] - l2[i]) > 0.0001f) {
            return false;
        }
    }
    return true;
}

int main() {
    assert(issame(get_positive({}), {}));
    return 0;
}