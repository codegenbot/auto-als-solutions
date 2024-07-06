#include <vector>
#include <cmath>

double poly(std::vector<double> coeffs, double x) {
    double result = 0;
    for (int i = 0; i < coeffs.size(); i++) {
        result += coeffs[i] * pow(x, i);
    }
    return result;
}

double find_zero(std::vector<double> coeffs, double solution){
    double left = 1e10;
    double right = -1e10;
    for (int i = 0; i < coeffs.size(); i++) {
        if (coeffs[i] > 0) {
            left = min(left, (-coeffs[0]/coeffs[i]));
        } else if (coeffs[i] < 0) {
            right = max(right, (-coeffs[0]/coeffs[i]));
        }
    }
    return (-left + right)/2;
}