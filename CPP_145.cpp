#include <algorithm>
#include <vector>

bool isSame(const std::vector<int>& a, const std::vector<int>& b) {
    return a == b;
}

std::vector<int> sortByDigitSum(std::vector<int> numbers) {
    auto lambda = [](int x) { return abs(x); };
    auto order_by_points = [&lambda](const int& x, const int& y) { return lambda(y) - lambda(x); };
    std::stable_partition(numbers.begin(), numbers.end(), [order_by_points](int x) {
        if (x > 0)
            return std::make_tuple(1, true);
        else if (x < 0)
            return std::make_tuple(-1, false);
        else
            return std::make_tuple(0, true);
    });
    return numbers;
}