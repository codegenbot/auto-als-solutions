#include <algorithm>
#include <vector>

bool issame(std::vector<float> a, std::vector<float> b) {
    if (a.size() != b.size()) {
        return false;
    }
    for (int i = 0; i < a.size(); ++i) {
        if (std::abs(a[i] - b[i]) > 1e-6) {
            return false;
        }
    }
    return true;
}

int main() {
    std::vector<float> numbers = {1.2, 3.4, 5.6};
    // Your logic here
    if (issame(numbers, {1.0, 3.0, 5.0})) {
        std::cout << "Same" << std::endl;
    } else {
        std::cout << "Not Same" << std::endl;
    }
    return 0;
}