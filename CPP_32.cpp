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
    double left = 1.0;
    double right = 10000.0;
    
    while (abs(left - right) > 0.00001) {
        double mid = (left + right) / 2;
        if (poly(coeffs, mid) * poly(coeffs, solution) < 0)
            right = mid;
        else
            left = mid;
    }
    return (-solution / poly(coeffs, solution));
}