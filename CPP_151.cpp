#include <iostream>
#include <cmath>
#include <vector>

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
    std::vector<float> lst = {1.5f, 3.0f, -4.25f, 6.0f};
    assert(double_the_difference(lst) == 15);
    std::cout << "The difference is: " << double_the_difference(lst) << std::endl;
    return 0;
}