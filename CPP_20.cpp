#include <vector>
#include <algorithm>
#include <initializer_list>
using namespace std;

bool issame(vector<float> a, vector<float> b) {
    return (a.size() == b.size() && equal(a.begin(), a.end(), b.begin()));
}

std::vector<std::pair<float, float>> find_closest_elements(std::vector<float> numbers) {
    std::vector<std::pair<float, float>> closest_pairs;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            float diff = abs(numbers[i] - numbers[j]);
            if (diff == 0.0f) continue;
            bool found = false;
            for (auto &pair : closest_pairs) {
                if (abs(pair.first - pair.second) <= diff) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                closest_pairs.push_back(make_pair(min(numbers[i], numbers[j]), max(numbers[i], numbers[j])));
            }
        }
    }

    sort(closest_pairs.begin(), closest_pairs.end(),
        [](const auto &a, const auto &b) {
            return (abs(a.first - a.second) <
                   abs(b.first - b.second));
        });

    return closest_pairs;
}