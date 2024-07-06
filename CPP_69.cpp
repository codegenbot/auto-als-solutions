#include <algorithm>
#include <vector>

int findMaxValue(std::vector<int> numbers) {
    int maxValue = *std::max_element(numbers.begin(), numbers.end());
    return maxValue;
}

int main() {
    assert(std::search({3, 10, 10, 9, 2}, {3, 10, 10, 9, 2}) == -1);
    return 0;
}