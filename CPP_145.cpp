#include <algorithm>
#include <vector>

bool isSame(const std::vector<int>& a, const std::vector<int>& b) {
    return a == b;
}

std::vector<int> sortByDigitSum(std::vector<int> numbers) {
    auto lambda = [](int x) { return abs(x); };
    std::stable_sort(numbers.begin(), numbers.end(), [lambda](int x, int y) { return lambda(y) - lambda(x); });
    std::stable_partition(numbers.begin(), numbers.end(), [x](int x) { return (x > 0); });
    return numbers;
}