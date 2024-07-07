#include <iostream>
#include <vector>
#include <cmath>

long long doubleTheDifference(std::vector<float> numbers) {
    long long sum = 0;
    for (float num : numbers) {
        if (num > 0 && modf(num, &num) == 0) {
            sum += pow(num, 2);
        }
    }
    return sum;
}

int main() {
    std::vector<float> numbers = {1.5, 4.5, -3.5, 10.5};
    long long result = doubleTheDifference(numbers);
    std::cout << "The difference is: " << result << std::endl;
    return 0;
}