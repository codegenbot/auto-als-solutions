#include <algorithm>
#include <limits>

vector<pair<float, float>> find_closest_elements(vector<float> numbers) {
    sort(numbers.begin(), numbers.end());
    float minDiff = numeric_limits<float>::max();
    vector<pair<float, float>> closestPairs;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        float diff = numbers[i + 1] - numbers[i];
        if (diff < minDiff) {
            minDiff = diff;
            closestPairs = {{numbers[i], numbers[i + 1]}};
        } else if (diff == minDiff) {
            closestPairs.push_back({numbers[i], numbers[i + 1]});
        }
    }

    return closestPairs;
}