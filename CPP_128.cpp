#include <cmath>

int prod_signs(int* arr, int n) {
    int product = 1;
    long long sum = 0;

    for (int i = 0; i < n; ++i) {
        if (arr[i] == 0) {
            return 0; 
        }
        product *= (arr[i] > 0 ? 1 : -1);
        sum += std::abs(arr[i]);
    }

    return (n == 0) ? -32768 : product * sum;
}