```cpp
#include <vector>
#include <cmath>

double poly(const std::vector<double>& coeffs, double x) {
    double result = 0;
    for (int i = 0; i < coeffs.size(); ++i) {
        result += coeffs[i] * pow(x, i);
    }
    return result;
}

double find_zero(std::vector<double> coeffs, double solution){
    double left = poly(coeffs, solution);
    double right = poly(coeffs, -solution);
    if (std::abs(left) < std::abs(right)) {
        return -solution;
    } else {
        return solution;
    }
}