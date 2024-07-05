```
#include <vector>
#include <cmath>

bool same(vector<float> a, vector<float> b) {
    if(a.size() != b.size())
        return false;
    for(int i = 0; i<a.size(); i++)
        if(abs(a[i] - b[i]) > 1e-9)
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

int main() {
    vector<float> v1 = get_positive({-1, 2, -3, 4});
    assert(same(get_positive(v1), {2, 4}));
    return 0;
}