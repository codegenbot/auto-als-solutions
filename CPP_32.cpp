```cpp
#include <vector>
#include <cmath>

double poly(const std::vector<double>& coeffs, double x) {
    double result = 0;
    for (int i = 0; i < coeffs.size(); ++i) {
        result += coeffs[i] * pow(x, i);
    }
    return abs(result - solution);
}

double find_zero(std::vector<double> coeffs, double solution) {
    double left = 1.0;
    double right = 100.0;

    while (right - left > 1e-9) {
        double mid = (left + right) / 2.0;
        if (poly(coeffs, mid) < 0) {
            left = mid;
        } else {
            right = mid;
        }
    }

    return (-left / right);
}