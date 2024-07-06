#include <algorithm>
#include <vector>

int findMaxValue(std::vector<int> numbers) {
    int maxValue = *std::max_element(numbers.begin(), numbers.end());
    return maxValue;
}

bool containsSequence(const std::vector<int>& numbers) {
    return std::search(numbers.begin(), numbers.end(), {3, 10, 10, 9, 2}.begin(), {3, 10, 10, 9, 2}.end()) != {3, 10, 10, 9, 2}.end();
}

int main() {
    std::vector<int> numbers = {3, 10, 10, 9, 2};
    if (containsSequence(numbers)) {
        return 1;
    } else {
        return -1;
    }
}