#include <vector>
#include <cmath>

bool isSame(const std::vector<float>& a, const std::vector<float>& b) {
    if (a.size() != b.size()) {
        return false;
    }
    for (int i = 0; i < a.size(); i++) {
        if (std::abs(a[i] - b[i]) > 1e-6) {
            return false;
        }
    }
    return true;
}

vector<float> derivative(vector<float> xs) {
    vector<float> result;
    for (int i = 0; i < xs.size() - 1; i++) {
        result.push_back((xs[i+1] - xs[i]) / static_cast<float>(1));
    }
    return result;
}

int main() {
    assert(isSame(derivative({0,1,2}), vector<float>({1}))); 
    return 0;
}