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
    double left = 1e9;
    double right = -1e9;
    for (int x = -100; x <= 100; ++x) {
        if (poly(coeffs, static_cast<double>(x)) > 0 && poly(coeffs, static_cast<double>(x+1)) < 0) {
            left = std::min(left, static_cast<double>(x));
            right = std::max(right, static_cast<double>(x));
        }
    }
    return (-left / right);
}