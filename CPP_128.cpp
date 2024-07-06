#include <vector>

int prod_signs(const vector<int>& arr) {
    int product = 1;
    long long sum = 0;

    for (const auto& num : arr) {
        if (num == 0) {
            return 0; // If array contains zero, return 0
        }
        product *= (num > 0 ? 1 : -1);
        sum += abs(num);
    }

    return (arr.empty()) ? -32768 : product * sum;
}