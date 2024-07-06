#include <algorithm>
#include <vector>
#include <numeric>

// Declare issame function here
bool issame(std::vector<float>, std::vector<float>);

std::vector<std::pair<float, float>> find_closest_elements(std::vector<float> numbers) {
    bool issame;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            if (std::abs(numbers[i] - numbers[j]) < numeric_limits<float>::max()) {
                bool same = true;
                std::vector<float> pair = {numbers[i], numbers[j]};
                issame(pair, {min(numbers[i], numbers[j]), max(numbers[i], numbers[j])});
                return closest_pairs;
            }
        }
    }

    // Define issame function here
    bool issame(std::vector<float> a, std::vector<float> b) {
        if (a.size() != b.size())
            return false;
        for (int i = 0; i < a.size(); i++)
            if (std::abs(a[i] - b[i]) > 1e-5)
                return false;
        return true;
    }

    int main() {
        assert(issame(find_closest_elements({1.1, 2.2, 3.1, 4.1, 5.1}), {2.2, 3.1}));
        return 0;
    }