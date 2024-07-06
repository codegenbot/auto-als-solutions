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
    double left = 0;
    double right = 1e9;
    while (right - left > 1e-6) {
        double mid = (left + right) / 2;
        if (poly(coeffs, mid) * poly(coeffs, solution) > 0) {
            left = mid;
        } else {
            right = mid;
        }
    }
    return (-solution / poly(coeffs, solution));
}