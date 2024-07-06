```cpp
#include <algorithm>
#include <vector>

int findMaxValue(std::vector<int> numbers) {
    int maxValue = *std::max_element(numbers.begin(), numbers.end());
    return maxValue;
}

bool containsSameSequence(const std::vector<int>& seq1, const std::vector<int>& seq2) {
    if (seq1.size() != seq2.size()) return false;
    return std::search(seq1.begin(), seq1.end(), seq2.begin(), seq2.end()) == seq1.end();
}

int main() {
    std::vector<int> numbers = {3, 10, 10, 9, 2};
    if (!containsSameSequence({3, 10, 10, 9, 2}, {3, 10, 10, 9, 2})) {
        return 1;
    }
    return 0;
}