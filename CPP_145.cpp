#include <algorithm>
#include <vector>

bool isSame(const std::vector<int>& a, const std::vector<int>& b) {
    return a == b;
}

std::vector<int> sortByDigitSum(std::vector<int> numbers) {
    std::stable_sort(numbers.begin(), numbers.end(), 
        [&](int x) { return abs(x); });
    return numbers;
}