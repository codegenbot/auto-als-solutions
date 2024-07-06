#include <cmath>
#include <iostream>
#include <vector>

void problemCPP133() {
    std::vector<float> lst = {1.2f, 3.5f, -0.8f};
    int result = sum_squares(lst);
    std::cout << "Sum of squares is: " << result << std::endl;
}

int sum_squares(std::vector<float> lst) {
    int result = 0;
    for (float x : lst) {
        int ceil_x = std::ceil(x);
        result += pow(ceil_x, 2);
    }
    return result;
}