```
#include <iostream>
#include <vector>
#include <cmath>

long long double_the_difference(std::vector<float> lst) {
    long long sum = 0;
    for (float num : lst) {
        if (num > 0 && std::floor(num) == num) { 
            if (num % 2 != 0) { 
                sum += pow(num, 2); 
            }
        }
    }
    return sum;
}

int main() {
    std::vector<float> lst = {1.5f, 3.8f, -4.2f, 6.7f};
    assert(double_the_difference(lst) == 20);
    std::cout << "The double difference is: " << double_the_difference(lst) << std::endl;
    return 0;
}