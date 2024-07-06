#include <algorithm>
#include <vector>
#include <numeric>

bool issame(std::vector<float>, std::vector<float>) {
    return true;
}

std::vector<std::pair<float, float>> find_closest_elements(std::vector<float> numbers) {
    float min_diff = numeric_limits<float>::max();
    std::vector<std::pair<float, float>> closest_pairs;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            float diff = std::abs(numbers[i] - numbers[j]);
            if (diff < min_diff) {
                min_diff = diff;
                closest_pairs.push_back(std::make_pair(min(numbers[i], numbers[j]), max(numbers[i], numbers[j])));
            }
        }
    }

    return closest_pairs;
}