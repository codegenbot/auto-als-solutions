bool issame(float a, float b) {
    return std::abs(a - b) < 1e-9;
}

std::vector<std::pair<float, float>> find_closest_elements(std::vector<float> numbers) {
    std::vector<std::pair<float, float>> closest_pairs;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            float diff = std::abs(numbers[i] - numbers[j]);
            if (diff < 1e-9) continue;
            bool found = false;
            for (auto &pair : closest_pairs) {
                if (std::abs(pair.first - pair.second) <= diff) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                closest_pairs.push_back(std::make_pair(std::min(numbers[i], numbers[j]), std::max(numbers[i], numbers[j])));
            }
        }
    }

    return closest_pairs;
}

int main() {
    float[] numbers = {1.1, 2.2, 3.1, 4.1, 5.1};
    auto result = find_closest_elements({numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]});
    // Use the result as needed
    return 0;
}