#include <cmath>
#include <vector>
#include <iostream>

std::vector<double> coeffs = {1.0, -7.0, 12.0, -6.0}; 

int main() {
    double solution = std::findZero(coeffs);

    std::cout << "The root is: " << solution << std::endl;
    std::cout << "The value of the polynomial at this root is: " << std::poly(coeffs, solution) << std::endl;

    return 0;
}