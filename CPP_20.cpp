```cpp
#include <algorithm>
#include <vector>
#include <numeric>

std::vector<std::pair<float, float>> find_closest_elements(std::vector<float> numbers) {
    std::vector<std::pair<float, float>> closest_pairs;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            float diff = std::abs(numbers[i] - numbers[j]);
            if (diff == 0.0f) continue;
            bool same_elements = false;

            if (std::find_if(closest_pairs.begin(), closest_pairs.end(),
                [&](const auto& pair) { return (pair.first <= std::min(numbers[i], numbers[j]) && pair.second >= std::max(numbers[i], numbers[j])); }) != closest_pairs.end()) {
                same_elements = true;
            }

            if (!same_elements) {
                closest_pairs.push_back(std::make_pair(std::min(numbers[i], numbers[j]), std::max(numbers[i], numbers[j])));
            }
        }
    }

    return closest_pairs;
}