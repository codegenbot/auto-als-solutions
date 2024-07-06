#include <vector>
#include <set>

bool issame(vector<float> l1, vector<float> l2) {
    if (l1.size() != l2.size()) {
        return false;
    }
    set<float> s1(l1.begin(), l1.end());
    set<float> s2(l2.begin(), l2.end());
    return s1 == s2;
}

int main() {
    assert(issame(get_positive({}), {}));
    return 0;
}

vector<float> get_positive(vector<float> l) {
    vector<float> result;
    for (float num : l) {
        if (num > 0) {
            result.push_back(num);
        }
    }
    return result;
}