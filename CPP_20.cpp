#include <algorithm>

vector<pair<float, float>> find_closest_elements(vector<float> numbers) {
    vector<pair<float, float>> closest;
    pair<float, float> smallest = make_pair(numbers[0], numbers[0]);
    for (int i = 1; i < numbers.size(); i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            if (abs(numbers[i] - numbers[j]) < abs(smallest.first - smallest.second)) {
                smallest = make_pair(min(numbers[i], numbers[j]), max(numbers[i], numbers[j]));
            }
        }
    }
    closest.push_back(smallest);
    return vector<float>({smallest.first, smallest.second});
}