#include <vector>

int prod_signs(std::vector<int> arr) {
    int sign_product = 1;
    long long sum_magnitude = 0;

    if (arr.empty()) {
        return -32768;
    }

    for (int num : arr) {
        if (num == 0) {
            return 0;
        }
        sign_product *= (num > 0 ? 1 : -1);
        sum_magnitude += abs(num);
    }

    return static_cast<int>(sum_magnitude * sign_product);
}