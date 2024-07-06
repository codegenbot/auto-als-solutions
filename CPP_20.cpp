#include <algorithm>

vector<pair<float, float>> find_closest_elements(vector<float> numbers) {
    int n = numbers.size();
    pair<float, float> result;
    float min_diff = numeric_limits<float>::max();

    for (int i = 0; i < n - 1; ++i) {
        for (int j = i + 1; j < n; ++j) {
            float diff = numbers[j] - numbers[i];
            if (abs(diff) < min_diff) {
                min_diff = abs(diff);
                result = make_pair(numbers[i], numbers[j]);
            }
        }
    }

    return {result};
}