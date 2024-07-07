#include <iostream>
#include <vector>
#include <cmath>

long long double_the_difference(const std::vector<float>& lst) {
    long long sum = 0;
    for (const float& num : lst) {
        if (num > 0 && modf(num, &num) == 0) {
            sum += pow(num, 2);
        }
    }
    return sum;
}

int main() {
    std::vector<float> numbers = {1.5, 3.0, -4.25, 2.0, 6.5};
    long long result = double_the_difference(numbers);
    std::cout << "The difference is: " << result << std::endl;
    return 0;
}