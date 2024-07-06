#include <algorithm>

vector<float> find_closest_elements(vector<float> numbers) {
    if (numbers.size() < 2) return {};
    vector<pair<float, float>> pairs;
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = i + 1; j <= numbers.size(); j++) {
            pairs.push_back({numbers[i], numbers[j]});
        }
    }

    sort(pairs.begin(), pairs.end(),
         [](const pair<float, float>& a, const pair<float, float>& b) {
             return abs(a.first - a.second) <
                    abs(b.first - b.second);
         });

    vector<float> result = {pairs[0].first, pairs[0].second};
    if (result[1] == result[0]) {
        for (int i = 1; i < numbers.size(); i++) {
            if (numbers[i] != result[0])
                return {result[0], numbers[i]};
        }
    }

    return result;
}