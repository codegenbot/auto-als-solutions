#include <vector>

bool is_equal_to_sum_even(int n) {
    for (int a = 2; a <= n; ++a) {
        if (n - a > a && is_equal_to_sum_even(n - a, a)) {
            return true;
        }
    }
    return false;
}

bool is_equal_to_sum_even(int n, int a) {
    vector<int> numbers;
    for (int b = 2; b <= n; ++b) {
        if (n - a - b > b && is_equal_to_sum_even(n - a - b, a, b)) {
            numbers.push_back(b);
            return true;
        }
    }
    return false;
}