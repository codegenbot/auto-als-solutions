#include <vector>
#include <algorithm>

int prod_signs(const int arr[], size_t n) {
    int product = 1;
    long long sum = 0;

    for (size_t i = 0; i < n; ++i) {
        if (arr[i] == 0) {
            return 0; // If array contains zero, return 0
        }
        product *= (arr[i] > 0 ? 1 : -1);
        sum += std::abs(arr[i]); 
    }

    return (n == 0) ? -32768 : product * sum;
}