#include <iostream>
#include <vector>
#include <cmath>

int sum_squares(const std::vector<double>& lst) {
    int sum = 0;
    for (double num : lst) {
        sum += num * num;
    }
    return sum;
}

int main() {
    std::vector<double> lst;
    double num;

    while ((std::cin >> num) && (!std::cin.peek())) { 
        lst.push_back(num);
    }

    int sum = sum_squares(lst);

    std::cout << "Sum of squares: " << sum << std::endl;
    return 0;
}