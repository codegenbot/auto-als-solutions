Here is the solution:

```cpp
#include <vector>

using namespace std;

int prod_signs(vector<int> arr) {
    int sign_product = 1;
    long sum_magnitudes = 0;

    for (int num : arr) {
        if (num == 0) {
            return 0;
        }
        if (num > 0) {
            sign_product *= 1;
        } else if (num < 0) {
            sign_product *= -1;
        }

        sum_magnitudes += abs(num);
    }

    if (arr.empty()) {
        return INT_MIN; // equivalent to -32768
    }

    return sum_magnitudes * sign_product;
}