#include <vector>
#include <cmath>

double poly(vector<double> coeffs, double x) {
    double result = 0;
    for (int i = 0; i < coeffs.size(); i++) {
        result += coeffs[i] * pow(x, i);
    }
    return abs(result - 1);
}

double find_zero(vector<double> coeffs, double solution){
    double left = coeffs[0];
    double right = coeffs[coeffs.size() - 1];
    return (-left / right);
}