```cpp
#include <vector>
using namespace std;

bool issame(vector<float> a, vector<float> b) {
    return a.size() == b.size() && all_of(a.begin(), a.end(), [&b](float x) { return find(b.begin(), b.end(), x) != b.end(); });
}

vector<float> derivative(vector<float> xs) {
    vector<float> result;
    for (int i = 1; i < xs.size(); i++) {
        result.push_back(i * xs[i]);
    }
    return result;
}

int main() {
    assert(issame(derivative({1}), {}));
    return 0;
}