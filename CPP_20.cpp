#include <iostream>
#include <vector>
#include <algorithm>

bool issame(std::vector<float> a, std::vector<float> b) {
    return (a.size() == b.size() && equal(a.begin(), a.end(), b.begin()));
}

std::vector<std::pair<float, float>> find_closest_elements(std::vector<float> numbers) {
    std::vector<std::pair<float, float>> closest_pairs;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            float diff = std::abs(numbers[i] - numbers[j]);
            if (diff == 0.0f) continue;
            if (std::find_if(closest_pairs.begin(), closest_pairs.end(),
                    [i, j, &numbers](const auto& pair) {
                return min(i, j) >= numbers[0] && max(i, j) <= numbers.back() &&
                       min(numbers[i], numbers[j]) > pair.first && max(numbers[i], numbers[j]) < pair.second;
            }) == closest_pairs.end()) {
                closest_pairs.push_back(std::make_pair(min(numbers[i], numbers[j]), max(numbers[i], numbers[j])));
            }
        }
    }

    return closest_pairs;
}