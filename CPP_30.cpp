#include <vector>
#include <cassert>

bool issame(const std::vector<float>& a, const std::vector<float>& b) {
    return a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin());
}

vector<vector<float>> get_positive(vector<vector<float>>& l) {
    vector<vector<float>> result;
    for (auto& num : l) {
        if (!num.empty()) {
            if (std::all_of(num.begin(), num.end(), [](float x){return x > 0;})) {
                result.push_back(num);
            }
        }
    }
    return result;
}

int main() {
    vector<vector<float>> l = {{1, -2, 3}, {4, -5, 6}, {-7, 8, 9}};
    assert(std::equal(get_positive(l).begin(), get_positive(l).end(), l.begin()));
    return 0;
}