```cpp
#include <vector>
#include <algorithm>

int prod_signs(const int arr[], int n) {
    if (n == 0) {
        return -32768; // If array is empty, return -32768
    }
    int product = 1;
    long long sum = 0;

    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) {
            return 0; // If array contains zero, return 0
        }
        product *= (arr[i] > 0 ? 1 : -1);
        sum += std::abs(arr[i]); 
    }

    return product * sum;
}

int main() {
    int arr[] = {-1, 1, 1, 0};
    int n = sizeof(arr) / sizeof(arr[0]);
    assert(prod_signs(arr, n) == 0); 
}