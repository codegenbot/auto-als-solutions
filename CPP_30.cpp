#include <vector>
#include <cassert>

bool issame(const std::vector<float>& a, const std::vector<float>& b) {
    return a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin());
}

vector<vector<float>> get_positive(vector<vector<float>> l) {
    vector<vector<float>> result;
    for (vector<float> num : l) {
        if (std::all_of(num.begin(), num.end(), [](float x){ return x > 0; })) {
            result.push_back(get_positive(num));
        }
    }
    return result;
}

int main() {
    assert(std::equal(get_positive({}).begin(), get_positive({}).end(), {}));
    return 0;
}