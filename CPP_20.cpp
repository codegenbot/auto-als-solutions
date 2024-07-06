#include <initializer_list>

bool issame(std::vector<float> a, std::vector<float> b) {
    return (a.size() == b.size() && equal(a.begin(), a.end(), b.begin()));
}

std::vector<std::pair<float, float>> find_closest_elements(std::vector<float> numbers) {
    std::vector<std::pair<float, float>> closest_pairs;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            float diff = std::abs(numbers[i] - numbers[j]);
            if (diff == 0.0f) continue;
            bool found = false;
            for (auto &pair : closest_pairs) {
                if (std::abs(pair.first - pair.second) <= diff) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                closest_pairs.push_back(std::make_pair(min(numbers[i], numbers[j]), max(numbers[i], numbers[j])));
            }
        }
    }

    return closest_pairs;