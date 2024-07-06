#include <algorithm>
#include <vector>

int findMaxValue(std::vector<int> numbers) {
    int maxValue = *std::max_element(numbers.begin(), numbers.end());
    return maxValue;
}

bool containsSequence(const std::vector<int>& numbers, const std::vector<int>& sequence) {
    return std::search(numbers.begin(), numbers.end(), sequence.begin(), sequence.end()) != sequence.end();
}

int main() {
    assert(!containsSequence({3, 10, 10, 9, 2}, {3, 10, 10, 9, 2}));
    return 0;
}