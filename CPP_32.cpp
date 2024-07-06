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
    for (int i = 0; i < coeffs.size(); ++i) {
        if (coeffs[i] > 0) {
            right = min(right, pow(solution, i));
        } else {
            left = max(left, pow(solution, i));
        }
    }
    return (-left + right) / (2 * abs(left - right));
}