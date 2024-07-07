```cpp
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
    std::vector<float> numbers = {1.5, 2.25, -3.75, 4.0};
    float odd_sum = 0;
    
    for (float num : numbers) {
        if (num > 0 && modf(num, &num) == 0) {
            odd_sum += pow(num, 2);
        }
    }
    
    long long result = double_the_difference(numbers);
    
    std::cout << "The sum of squares is: " << result << std::endl;
    std::cout << "The sum of squares of odd numbers is: " << odd_sum << std::endl;
    
    return 0;
}