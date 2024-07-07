#include <iostream>
#include <vector>
#include <cmath>

long long double_the_difference(const std::vector<float>& lst) {
    long long sum = 0;
    for (float num : lst) {
        if (num > 0 && floor(num) == num) { 
            if (num % 2 != 0) { 
                sum += pow(num, 2); 
            }
        }
    }
    return sum;
}

int main() {
    std::vector<float> lst = {1.5f, 3.8f, 4.9f, -1.7f, 2.2f};
    assert(double_the_difference(lst) == 19);
    
    for (float num : lst) {
        if (num > 0 && floor(num) == num) { 
            if (num % 2 != 0) { 
                std::cout << "Square of the number: " << pow(num, 2) << std::endl;
            }
        }
    }

    return 0;
}