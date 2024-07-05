#include <vector>
#include <assert.h>

bool is_same(vector<float> a, vector<float> b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i<a.size(); i++)
        if (abs(a[i] - b[i]) > 1e-9)
            return false;
    return true;
}

vector<float> get_positive(vector<float> l) {
    vector<float> result;
    for (float x : l) {
        if (x > 0)
            result.push_back(x);
    }
    return result;
}

int calculate() {
    assert(is_same(get_positive({}), {}) == true);
    return 0;
}

int main() {
    calculate();
    return 0;
}