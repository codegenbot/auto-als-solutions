#include <vector>
#include <cmath>

double find_zero(std::vector<double> coeffs, double solution) {
    double left = coeffs[0];
    double right = coeffs[coeffs.size() - 1];
    return (-left / right);
}