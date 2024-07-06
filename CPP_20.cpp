#include <iostream>
#include <vector>
#include <algorithm>

bool issame(const float& a, const float& b) {
    if (std::abs(a - b) <= std::numeric_limits<float>::epsilon()) return true;
    else return false;
}

std::vector<std::pair<float, float>> find_closest_elements(std::vector<float> numbers) {
    std::vector<std::pair<float, float>> closest_pairs;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            if (issame(numbers[i], numbers[j])) continue;
            if (std::find(closest_pairs.begin(), closest_pairs.end(), std::pair<float, float>(min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))) == closest_pairs.end()) {
                closest_pairs.push_back(std::make_pair(min(numbers[i], numbers[j]), max(numbers[i], numbers[j])));
            }
        }
    }

    return closest_pairs;
}