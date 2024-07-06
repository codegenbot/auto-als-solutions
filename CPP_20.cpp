#include <algorithm>
#include <vector>
#include <numeric>
#include <limits>

bool same(std::vector<float> a, std::vector<float> b) {
    if (a.size() != b.size())
        return false;
    for (int i = 0; i < a.size(); i++) {
        if (std::abs(a[i] - b[i]) > std::numeric_limits<float>::epsilon())
            return false;
    }
    return true;
}

std::vector<std::pair<float, float>> find_closest_elements(std::vector<float> numbers) {
    std::vector<std::pair<float, float>> closest_pairs;
    float min_diff = std::numeric_limits<float>::max();

    for (int i = 0; i < numbers.size() - 1; ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            float diff = std::abs(numbers[i] - numbers[j]);
            if (diff < min_diff) {
                min_diff = diff;
                closest_pairs.clear();
                closest_pairs.push_back(std::make_pair(min(numbers[i], numbers[j]), max(numbers[i], numbers[j])));
            } else if (diff == min_diff) {
                closest_pairs.push_back(std::make_pair(min(numbers[i], numbers[j]), max(numbers[i], numbers[j])));
            }
        }
    }

    return closest_pairs;
}

int main() {
    assert(same(find_closest_elements({1.1, 2.2, 3.1, 4.1, 5.1}), {2.2, 3.1}));
    return 0;
}