```cpp
#include <iostream>
#include <vector>
#include <cmath>

long long sum_squares(const std::vector<float>& lst) {
    long long result = 0;
    for (float x : lst) {
        long long ceil_x = std::lround(x);
        result += pow(ceil_x, 2);
    }
    return result;
}

int main() {
    std::vector<float> lst;
    float num;

    while (std::cin >> num) {
        lst.push_back(num);
    }

    long long sum = sum_squares(lst);

    std::cout << "Sum of squares: " << sum << std::endl;
}