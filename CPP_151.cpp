#include <iostream>
#include <cmath>
#include <vector>

long long double_the_difference(std::vector<float> lst) {
    long long sum = 0;
    for (float num : lst) {
        if (num > 0 && std::floor(num) == num) { // Check if number is positive and integer
            if (num % 2 != 0) { // Check if number is odd
                sum += pow(num, 2); // Add square of the number to sum
            }
        }
    }
    return sum;
}

int main() {
    std::vector<float> lst = {1.5f, 3.0f, -4.5f, 6.0f};
    assert(double_the_difference(lst) == 14);
    return 0;
}