#include <vector>
#include <algorithm>

std::pair<float, float> find_closest_elements(std::vector<float> numbers) {
    if (numbers.size() < 2) {
        return {0.0f, 0.0f}; // or throw an exception if you prefer
    }

    std::pair<float, float> closest_pair = {numbers[0], numbers[1]};
    float min_diff = abs(numbers[0] - numbers[1]);

    for (int i = 0; i < numbers.size() - 1; ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            float diff = abs(numbers[i] - numbers[j]);
            if (diff < min_diff) {
                min_diff = diff;
                closest_pair = {numbers[i], numbers[j]};
            }
        }
    }

    return closest_pair;
}