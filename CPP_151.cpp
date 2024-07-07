#include <iostream>
#include <vector>
#include <cmath>

long long double_the_difference(std::vector<float> lst) {
    long long sum = 0;
    for (float num : lst) {
        if (num > 0 && modf(num, &num) == 0) {
            sum += pow(num, 2);
        }
    }
    return sum;
}

int main() {
    std::vector<float> numbers = {1.5, 3.4, -7.8, 9.9};
    float odd_sum = 0;

    for (float num : numbers) {
        if (num > 0 && modf(num, &num) == 0) {
            odd_sum += pow(num, 2);
        }
    }

    long long sum = double_the_difference(numbers);

    std::cout << "Odd sum: " << odd_sum << std::endl;
    std::cout << "Double the difference: " << sum << std::endl;

    return 0;
}