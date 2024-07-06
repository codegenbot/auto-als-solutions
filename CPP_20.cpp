#include <algorithm>
#include <vector>
#include <numeric>

std::vector<std::pair<float, float>> find_closest_elements(std::vector<float> numbers) {
    std::vector<std::pair<float, float>> closest_pairs;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            float diff = std::abs(numbers[i] - numbers[j]);
            if (diff == 0.0f) continue;
            if (diff < std::numeric_limits<float>::max()) {
                if (std::find(closest_pairs.begin(), closest_pairs.end(), std::pair<float, float>(numbers[i], numbers[j])) == closest_pairs.end()) {
                    closest_pairs.push_back(std::make_pair(min(numbers[i], numbers[j]), max(numbers[i], numbers[j])));
                }
            }
        }
    }

    return closest_pairs;
}