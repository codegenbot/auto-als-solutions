#include <vector>
#include <cmath>

double poly(std::vector<double> coeffs, double x) {
    double result = 0;
    for (int i = 0; i < coeffs.size(); ++i) {
        result += coeffs[i] * pow(x, i);
    }
    return result;
}

double find_zero(std::vector<double> coeffs, double solution){
    double left = -coeffs[1];
    double right = coeffs[0];
    for (int i = 2; i < coeffs.size(); ++i) {
        if (poly(coeffs, solution) != 0)
            break;
        solution -= poly(coeffs, solution) / poly(coeffs, solution);
    }
    return solution;
}