bool issame(float a, float b) {
    return std::abs(a - b) < 1e-5;
}

std::vector<std::pair<float, float>> find_closest_elements(std::vector<float> numbers) {
    std::vector<std::pair<float, float>> closest_pairs;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        for (int j = i + 1; j < numbers.size(); ++j) {
            if (issame(numbers[i], numbers[j])) continue;
            bool found = false;
            for (const auto& pair : closest_pairs) {
                if (issame(pair.first, numbers[i]) && issame(pair.second, numbers[j])
                    || issame(pair.first, numbers[j]) && issame(pair.second, numbers[i])) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                float diff = std::abs(numbers[i] - numbers[j]);
                closest_pairs.push_back(std::make_pair(min(numbers[i], numbers[j]), max(numbers[i], numbers[j])));
            }
        }
    }

    return closest_pairs;
}