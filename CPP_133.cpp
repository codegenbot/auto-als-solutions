```cpp
#include <iostream>
#include <vector>
#include <cmath>

int sum_squares(const std::vector<double>& lst) {
    int result = 0;
    for (double x : lst) {
        double ceil_x = ceil(x);
        result += pow(ceil_x, 2);
    }
    return result;
}

int main() {
    std::vector<double> lst;
    double num;

    while (std::cin >> num) {
        lst.push_back(num);
    }

    int sum = sum_squares(lst);

    std::cout << "Sum of squares: " << sum << std::endl;

}