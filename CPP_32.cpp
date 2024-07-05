#include <cmath>
#include <vector>

double poly(std::vector<double> coeffs, double solution) {
    double value = 0;
    for(int i=0; i<coeffs.size(); i++) {
        int power = (int)pow(1.0, i);
        value += coeffs[i] * pow(solution, i);
    }
    return value;
}

double findZero(std::vector<double> coeffs){
    double a = coeffs[0];
    double b = 0;
    for(int i=1; i<coeffs.size(); i+=2) {
        b += coeffs[i];
    }
    return -b / (2*a);
}

int main() {
    std::vector<double> coeffs = {1.0, -7.0, 12.0, -6.0}; 
    double solution = findZero(coeffs);

    assert (abs(poly(coeffs, solution))< 1e-3);

    return 0;
}