```cpp
bool issame(float a, float b) {
    return (a - 0.5f < b && b - 0.5f < a);
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
                closest_pairs.push_back(std::make_pair(min(numbers[i], numbers[j]), max(numbers[i], numbers[j])));
            }
        }
    }

    return closest_pairs;
}

int main() {
    float[] numbers = {1.1, 2.2, 3.1, 4.1, 5.1};
    std::vector<float> vec(numbers, numbers + sizeof(float) / sizeof(float));
    std::vector<std::pair<float, float>> closest = find_closest_elements(vec);
    return 0;
}