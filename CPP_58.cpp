```cpp
#include <vector>
#include <algorithm>

using namespace std;

vector<int> common(vector<int> a, vector<int> b) {
    set<int> bSet(b.begin(), b.end());
    vector<int> result;
    for (int i = 0; i < a.size(); i++) {
        if (bSet.count(a[i])) {
            result.push_back(a[i]);
            bSet.erase(a[i]);
        }
    }
    return result;
}

bool issame(vector<int> a, vector<int> b) {
    return is_permutation(a.begin(), a.end(), b.begin(), b.end());
}

int main() {
    assert(common({4, 3, 2, 8}, {}) == {});
}