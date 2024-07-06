#include <vector>
#include <algorithm>
#include <initializer_list>

bool issame(std::vector<float> a, std::vector<float> b) {
    return (a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin()));
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
                closest_pairs.push_back(std::make_pair(std::min(numbers[i], numbers[j]), std::max(numbers[i], numbers[j])));
            }
        }
    }

    return closest_pairs;
}

int main() {
    int numElements;
    float *numbers;

    std::cout << "Enter the number of elements: ";
    std::cin >> numElements;

    numbers = new float[numElements];

    for (int i = 0; i < numElements; ++i) {
        std::cout << "Enter element " << i + 1 << ": ";
        std::cin >> numbers[i];
    }

    std::vector<float> nums(numbers, numbers + numElements);
    std::vector<std::pair<float, float>> closest = find_closest_elements(nums);

    if (!closest.empty()) {
        std::cout << "Closest elements: ";
        for (auto &pair : closest) {
            std::cout << "(" << pair.first << ", " << pair.second << ") ";
        }
        std::cout << std::endl;
    } else {
        std::cout << "No closest elements found." << std::endl;
    }

    delete[] numbers;
    
    return 0;
}