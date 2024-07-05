#include <vector>
#include <cmath>

bool same(vector<float> a, vector<float> b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i<a.size(); i++)
        if (abs(a[i] - b[i]) > 1e-9)
            return false;
    return true;
}

vector<float> get_positives(vector<float> l) {
    vector<float> result;
    for (float x : l) {
        if (x > 0)
            result.push_back(x);
    }
    return result;
}

int test() {
    assert(same(get_positives({}), {}));
    return 0;
}