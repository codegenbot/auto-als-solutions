#include <iostream>
#include <vector>
#include <cmath>

int sum_squares(const std::vector<float>& lst) {
    int result = 0;
    for (float x : lst) {
        int ceil_x = ceil(x);
        result += pow(ceil_x, 2);
    }
    return result;
}

int main {
    std::vector<float> lst;
    float num;

    while(std::cin >> num) {
        lst.push_back(num);
    }

    int sum = sum_squares(lst);

    std::cout << "Sum of squares: " << sum << std::endl;

    return 0;
}