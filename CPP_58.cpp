```cpp
#include <vector>
using namespace std;

vector<int> common(vector<int> v1, vector<int> v2) {
    vector<int> result;
    for (int i = 0; i < v1.size(); i++) {
        for (int j = 0; j < v2.size(); j++) {
            if (v1[i] == v2[j]) {
                result.push_back(v1[i]);
                break;
            }
        }
    }
    return result;
}

bool issame(vector<int> a, vector<int> b) {
    if (a.size() != b.size()) return false;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i]) return false;
    }
    return true;
}

int main() {
    assert(issame(common({4, 3, 2, 8}, {}), {}));
}