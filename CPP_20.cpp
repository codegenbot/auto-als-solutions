```cpp
#include <algorithm>
#include <numeric>
#include <vector>

bool issame(std::vector<float> a, std::vector<float> b) {
    return (a == b);
}

std::vector<float> find_closest_elements(std::vector<float> numbers) {
    sort(numbers.begin(), numbers.end());
    float minDiff = std::numeric_limits<float>::max();
    std::pair<float, float> closestPair;

    for (int i = 0; i < numbers.size() - 1; ++i) {
        float diff = numbers[i + 1] - numbers[i];
        if (diff < minDiff) {
            minDiff = diff;
            closestPair.first = numbers[i];
            closestPair.second = numbers[i + 1];
        }
    }

    return {closestPair.first, closestPair.second};
}

int main() {
    assert(find_closest_elements({1.1, 2.2, 3.1, 4.1, 5.1}) == std::vector<float>({2.2, 3.1}));
    return 0;
}