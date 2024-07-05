#include <vector>
#include <cmath>

bool vectorEqual(std::vector<float> a, std::vector<float> b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i<a.size(); i++)
        if (std::abs(a[i] - b[i]) > 1e-9)
            return false;
    return true;
}

std::vector<float> getPositives(std::vector<float> l) {
    std::vector<float> result;
    for (float x : l) {
        if (x > 0)
            result.push_back(x);
    }
    return result;
}

int main() {
    assert(vectorEqual(getPositives({}), {}));
    return 0;
}